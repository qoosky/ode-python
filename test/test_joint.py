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

from .utils.nearcallback import NearCallbackBounceGround

class TestJoint(object):

    debug = False

    @fixture
    def ballGeom(self, world, space):
        mass = dMass()
        m = 1.0
        r = 0.2
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        ballBody = dBodyCreate(world)
        dBodySetMass(ballBody, byref(mass))
        ballGeom = dCreateSphere(space, r)
        dGeomSetBody(ballGeom, ballBody)
        return ballGeom

    @fixture
    def legGeom(self, world, space):
        m = 0.001
        r = 0.025
        l = 1.0
        direction = 3
        mass = dMass()
        dMassSetZero(byref(mass))
        dMassSetCapsuleTotal(byref(mass), m, direction, r, l)
        legBody = dBodyCreate(world)
        dBodySetMass(legBody, byref(mass))
        legGeom = dCreateCapsule(space, r, l)
        dGeomSetBody(legGeom, legBody)
        return legGeom

    @fixture
    def robotGeom(self, world, ballGeom, legGeom):
        ballBody = dGeomGetBody(ballGeom)
        legBody = dGeomGetBody(legGeom)

        pos = [0.0, 0.0, 2.5]
        dBodySetPosition(ballBody, pos[0], pos[1], pos[2])

        rBall = dGeomSphereGetRadius(ballGeom)
        rLeg = dReal()
        lLeg = dReal()
        dGeomCapsuleGetParams(legGeom, byref(rLeg), byref(lLeg))
        dBodySetPosition(legBody, pos[0], pos[1], pos[2] - (rBall + lLeg.value / 2.0))

        joint = dJointCreateHinge(world, 0)
        dJointAttach(joint, ballBody, legBody)
        dJointSetHingeAnchor(joint, pos[0], pos[1], pos[2] - rBall)
        dJointSetHingeAxis(joint, 1, 0, 0)

        dJointSetHingeParam(joint, dParamLoStop, 0)
        dJointSetHingeParam(joint, dParamHiStop, 0)
        # pi = 3.14159
        # dJointSetHingeParam(joint, dParamLoStop, -pi / 2.0)
        # dJointSetHingeParam(joint, dParamHiStop, pi / 2.0)
        # dJointSetHingeParam(joint, dParamLoStop, -pi)
        # dJointSetHingeParam(joint, dParamHiStop, pi)
        return ballGeom, legGeom

    @fixture
    def g(self):
        return [0.0, 0.1, -9.80665]

    def test_joint(self, world, space, contactgroup, ground, robotGeom):
        nearCallback = NearCallbackBounceGround(world=world, contactgroup=contactgroup, groundGeom=ground)

        if self.debug:
            from .utils.drawstuff import Drawstuff
            Drawstuff(world=world, geoms=list(robotGeom), space=space, contactgroup=contactgroup, nearCallback=nearCallback.Callback).Run()

        tDelta = 0.01
        for i in range(999):
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            assert(dWorldStep(world, tDelta) == 1)
            dJointGroupEmpty(contactgroup)
