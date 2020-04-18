# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref

from odepy import dBodyCreate
from odepy import dBodySetMass
from odepy import dBodySetPosition
from odepy import dCreateCapsule
from odepy import dCreateSphere
from odepy import dGeomCapsuleGetParams
from odepy import dGeomGetBody
from odepy import dGeomSetBody
from odepy import dGeomSphereGetRadius
from odepy import dJointAttach
from odepy import dJointCreateHinge
from odepy import dJointCreateSlider
from odepy import dJointGetSliderPosition
from odepy import dJointGroupEmpty
from odepy import dJointSetHingeAnchor
from odepy import dJointSetHingeAxis
from odepy import dJointSetHingeParam
from odepy import dJointSetSliderAxis
from odepy import dJointSetSliderParam
from odepy import dMass
from odepy import dMassSetCapsuleTotal
from odepy import dMassSetSphereTotal
from odepy import dMassSetZero
from odepy import dNearCallback
from odepy import dParamFMax
from odepy import dParamHiStop
from odepy import dParamLoStop
from odepy import dParamVel
from odepy import dReal
from odepy import dSpaceCollide
from odepy import dWorldSetCFM
from odepy import dWorldSetERP
from odepy import dWorldStep

from .utils.nearcallback import NearCallbackBounceGround

class BeforeStepCallbackTestJoint2(object):

    def __init__(self, jointSlider):
        self.__jointSlider = jointSlider
        self.__step = 0

    def Callback(self):
        s = 200
        self.__step += 1
        if 0 <= self.__step % s and self.__step % s <= 10:
            target = 0.5
        else:
            target = 0.0

        kp = 25.0  # PID (proportional - integral - derivative)
        fmax = 600  # Force Max [N]
        currentSliderPosition = dJointGetSliderPosition(self.__jointSlider)
        u = kp * (target - currentSliderPosition)
        dJointSetSliderParam(self.__jointSlider, dParamVel, u)
        dJointSetSliderParam(self.__jointSlider, dParamFMax, fmax)

class TestJoint2(object):

    debug = False

    @fixture
    def ballGeom(self, world, space):
        mass = dMass()
        m = 10.0
        r = 0.2
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        ballBody = dBodyCreate(world)
        dBodySetMass(ballBody, byref(mass))
        ballGeom = dCreateSphere(space, r)
        dGeomSetBody(ballGeom, ballBody)
        return ballGeom

    @fixture
    def legGeoms(self, world, space):
        legGeoms = []
        for m, l, r in [(2.0, 0.7, 0.04),
                        (2.0, 0.7, 0.02)]:
            direction = 3
            mass = dMass()
            dMassSetZero(byref(mass))
            dMassSetCapsuleTotal(byref(mass), m, direction, r, l)
            legBody = dBodyCreate(world)
            dBodySetMass(legBody, byref(mass))
            legGeom = dCreateCapsule(space, r, l)
            dGeomSetBody(legGeom, legBody)
            legGeoms.append(legGeom)
        return legGeoms

    @fixture
    def robot(self, world, ballGeom, legGeoms):
        ballBody = dGeomGetBody(ballGeom)
        legBodies = [dGeomGetBody(legGeom) for legGeom in legGeoms]

        rBall = dGeomSphereGetRadius(ballGeom)
        lLegs = []
        for legGeom in legGeoms:
            rLeg = dReal()
            lLeg = dReal()
            dGeomCapsuleGetParams(legGeom, byref(rLeg), byref(lLeg))
            lLegs.append(lLeg.value)

        pos = [0.0, 0.0, 1.5]
        dBodySetPosition(ballBody, pos[0], pos[1], pos[2])

        for i, legBody in enumerate(legBodies):
            if i == 0:
                z = pos[2] - (rBall + lLegs[0] / 2.0)
                dBodySetPosition(legBody, pos[0], pos[1], z)
            elif i == 1:
                z = pos[2] - (rBall + lLegs[0])
                dBodySetPosition(legBody, pos[0], pos[1], z)
            else:
                raise Exception('robot has two leg geoms.')

        jointSlider = dJointCreateSlider(world, 0)
        dJointAttach(jointSlider, legBodies[0], legBodies[1])
        dJointSetSliderAxis(jointSlider, 0, 0, 1)
        dJointSetSliderParam(jointSlider, dParamLoStop, -lLegs[1] / 2.0)
        dJointSetSliderParam(jointSlider, dParamHiStop, lLegs[1] / 2.0)

        jointHinge = dJointCreateHinge(world, 0)
        dJointAttach(jointHinge, ballBody, legBodies[0])
        dJointSetHingeAnchor(jointHinge, pos[0], pos[1], pos[2] - rBall)
        dJointSetHingeAxis(jointHinge, 1, 0, 0)
        dJointSetHingeParam(jointHinge, dParamLoStop, 0)
        dJointSetHingeParam(jointHinge, dParamHiStop, 0)

        return {
            'geoms': [ballGeom, legGeoms[0], legGeoms[1]],
            'joints': [jointSlider, jointHinge],
        }

    def test_joint2(self, world, space, contactgroup, ground, robot):

        nearCallback = NearCallbackBounceGround(world=world, contactgroup=contactgroup, groundGeom=ground)
        jointSlider = robot['joints'][0]

        dWorldSetERP(world, 1.0)
        dWorldSetCFM(world, 0.0)

        beforeStepCallbackTestJoint2 = BeforeStepCallbackTestJoint2(jointSlider=jointSlider)

        def commandCallback(cmd):
            print('cmd={}'.format(cmd))

        if self.debug:
            from .utils.drawstuff import Drawstuff
            Drawstuff(world=world,
                      geoms=robot['geoms'],
                      space=space,
                      contactgroup=contactgroup,
                      beforeStepCallback=beforeStepCallbackTestJoint2.Callback,
                      nearCallback=nearCallback.Callback,
                      commandCallback=commandCallback,
                      sphereQuality=3).Run()

        tDelta = 0.01
        for i in range(999):
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            assert(dWorldStep(world, tDelta) == 1)
            dJointGroupEmpty(contactgroup)
