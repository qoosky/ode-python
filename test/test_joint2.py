# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref

from odepy import dNearCallback
from odepy import dWorldStep
from odepy import dSpaceCollide
from odepy import dJointAttach
from odepy import dJointGroupEmpty
from odepy import dMass
from odepy import dMassSetCapsuleTotal
from odepy import dBodyCreate
from odepy import dMassSetSphereTotal
from odepy import dMassSetZero
from odepy import dBodySetMass
from odepy import dBodySetPosition
from odepy import dCreateCapsule
from odepy import dGeomSetBody
from odepy import dGeomGetBody
from odepy import dCreateSphere
from odepy import dJointCreateHinge
from odepy import dJointSetHingeAxis
from odepy import dJointSetHingeAnchor
from odepy import dJointSetHingeParam
from odepy import dGeomSphereGetRadius
from odepy import dReal
from odepy import dGeomCapsuleGetParams
from odepy import dParamLoStop
from odepy import dParamHiStop
from odepy import dJointCreateSlider
from odepy import dJointSetSliderAxis
from odepy import dJointSetSliderParam
from odepy import dWorldSetERP
from odepy import dWorldSetCFM
from odepy import dJointSetSliderParam
from odepy import dParamVel
from odepy import dParamFMax
from odepy import dJointGetSliderPosition
from odepy import dJointGetHingeAngle
from odepy import dJointAddHingeTorque
from odepy import dJointGetHingeAngleRate

from .utils.nearcallback import NearCallbackBounceGround

class TestJoint2(object):

    debug = False

    @fixture
    def ballGeom(self, world, space):
        mass = dMass()
        m = 14.0
        r = 0.25
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
        for m, l, r in [(3.0, 0.75, 0.05),
                        (3.0, 0.75, 0.03)]:
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
    def robotGeom(self, world, ballGeom, legGeoms):
        ballBody = dGeomGetBody(ballGeom)
        legBodies = [dGeomGetBody(legGeom) for legGeom in legGeoms]

        pos = [0.0, 0.0, 1.5]
        dBodySetPosition(ballBody, pos[0], pos[1], pos[2])

        rBall = dGeomSphereGetRadius(ballGeom)
        for i, (legGeom, legBody) in enumerate(zip(legGeoms, legBodies)):
            rLeg = dReal()
            lLeg = dReal()
            dGeomCapsuleGetParams(legGeom, byref(rLeg), byref(lLeg))
            if i == 0:
                z = pos[2] - (rBall + lLeg.value / 2.0)
            elif i == 1:
                z = pos[2] - (rBall + lLeg.value / 2.0) - 0.5
            else:
                raise
            dBodySetPosition(legBody, pos[0], pos[1], z)

        jointHinge = dJointCreateHinge(world, 0)
        dJointAttach(jointHinge, ballBody, legBodies[0])
        dJointSetHingeAnchor(jointHinge, pos[0], pos[1], pos[2] - rBall)
        dJointSetHingeAxis(jointHinge, 1, 0, 0)

        jointSlider = dJointCreateSlider(world, 0)
        dJointAttach(jointSlider, legBodies[0], legBodies[1])
        dJointSetSliderAxis(jointSlider, 0, 0, 1)
        dJointSetSliderParam(jointSlider, dParamLoStop, -0.25)
        dJointSetSliderParam(jointSlider, dParamHiStop, 0.25)

        # dJointSetHingeParam(joint, dParamLoStop, 0)
        # dJointSetHingeParam(joint, dParamHiStop, 0)
        # pi = 3.14159
        # dJointSetHingeParam(joint, dParamLoStop, -pi / 2.0)
        # dJointSetHingeParam(joint, dParamHiStop, pi / 2.0)
        # dJointSetHingeParam(joint, dParamLoStop, -pi)
        # dJointSetHingeParam(joint, dParamHiStop, pi)
        return ballGeom, legGeoms[0], legGeoms[1], jointSlider, jointHinge

    def test_joint2(self, world, space, contactgroup, ground, robotGeom):
        assert True

        # nearCallback = NearCallbackBounceGround(world=world, contactgroup=contactgroup, groundGeom=ground)
        # jointSlider = robotGeom[3]
        # jointHinge = robotGeom[4]

        # dWorldSetERP(world, 1.0)
        # dWorldSetCFM(world, 0.0)

        # class Hoge(object):
        #     def __init__(self):
        #         self.__step = 0
        #     def stepCallback(self):
        #         s = 200
        #         self.__step += 1
        #         if 0 <= self.__step % s and self.__step % s <= 10:
        #             target = 0.5
        #         else:
        #             target = 0.0

        #         kp = 25.0
        #         # fmax = 400
        #         fmax = 600
        #         tmp = dJointGetSliderPosition(jointSlider)
        #         u = kp * (target - tmp)
        #         dJointSetSliderParam(jointSlider, dParamVel, u)
        #         dJointSetSliderParam(jointSlider, dParamFMax, fmax)

        #         kp2 = 5.0
        #         fmax2 = 800
        #         tmp2 = dJointGetHingeAngle(jointHinge)
        #         u2 = kp2 * (target - tmp2)
        #         # dJointSetHingeParam(jointHinge, dParamVel, u2)
        #         # dJointSetHingeParam(jointHinge, dParamFMax, fmax2)

        #         kp3 = 100
        #         kt3 = 2.0
        #         tmp3 = dJointGetHingeAngle(jointHinge)
        #         u3 = kp3 * (target - tmp3)
        #         omega3 = dJointGetHingeAngleRate(jointHinge)
        #         trq3 = kt3 * omega3
        #         dJointAddHingeTorque(jointHinge, u3 - trq3)

        # hoge = Hoge()

        # if self.debug:
        #     from .utils.drawstuff import Drawstuff
        #     Drawstuff(world=world,
        #               geoms=list(robotGeom[:3]),
        #               space=space,
        #               contactgroup=contactgroup,
        #               stepCallback=hoge.stepCallback,
        #               nearCallback=nearCallback.Callback,
        #     ).Run()

        # tDelta = 0.01
        # for i in range(999):
        #     dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
        #     assert(dWorldStep(world, tDelta) == 1)
        #     dJointGroupEmpty(contactgroup)
