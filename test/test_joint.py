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
from odepy import dCreateSphere
from odepy import dBodyGetPosition
from odepy import dJointCreateHinge
from odepy import dJointGroupCreate
from odepy import dJointSetHingeAxis
from odepy import dJointSetHingeAnchor
from odepy import dJointSetHingeParam

from .utils.nearcallback import NearCallbackBounceGround

class TestJoint(object):

    @fixture
    def robot(self, world, space):
        mass = dMass()
        pos = [0.0, 0.0, 2.5]
        ballBody = dBodyCreate(world)
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), 1.0, 0.2)
        dBodySetMass(ballBody, byref(mass))
        dBodySetPosition(ballBody, pos[0], pos[1], pos[2])
        ballGeom = dCreateSphere(space, 0.2)
        dGeomSetBody(ballGeom, ballBody)

        legBody = dBodyCreate(world)
        dMassSetZero(byref(mass))
        dMassSetCapsuleTotal(byref(mass), 0.001, 3, 0.025, 1.0)
        dBodySetMass(legBody, byref(mass))
        dBodySetPosition(legBody, pos[0], pos[1], pos[2] - 0.2 - 0.5*1.0)
        legGeom = dCreateCapsule(space, 0.025, 1.0)
        dGeomSetBody(legGeom, legBody)

        hogegroup = dJointGroupCreate(1)

        joint = dJointCreateHinge(world, hogegroup)
        dJointAttach(joint, ballBody, legBody)
        dJointSetHingeAnchor(joint, 0.0, 0.0, 2.5 - 0.2)
        dJointSetHingeAxis(joint, 1, 0, 0)
        from numpy import pi
        dParamLoStop = 0
        dParamHiStop = 1
        dJointSetHingeParam(joint, dParamLoStop, -0.25 * pi)
        dJointSetHingeParam(joint, dParamHiStop, 0.25 * pi)
        # dJointSetHingeParam(joint, dParamLoStop, 0)
        # dJointSetHingeParam(joint, dParamHiStop, 0)
        # dJointSetHingeParam(joint, dParamLoStop, -pi)
        # dJointSetHingeParam(joint, dParamHiStop, pi)

        return ballGeom, legGeom

    def test_joint(self, world, space, contactgroup, ground, robot):
        nearCallback = NearCallbackBounceGround(world=world, contactgroup=contactgroup, groundGeom=ground)

        tDelta = 0.01
        z0 = 3.0

        if True:
            from .utils.drawstuff import Drawstuff
            Drawstuff(world=world, geoms=[robot[0], robot[1]], space=space, contactgroup=contactgroup, nearCallback=nearCallback.Callback).Run()

        for i in range(99):
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            dWorldStep(world, tDelta)
            dJointGroupEmpty(contactgroup)
            # pos = dBodyGetPosition(robot[0])
            # print(pos[2])
