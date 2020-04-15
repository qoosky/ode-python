# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref
from ctypes import addressof
from ctypes import sizeof

from odepy import dWorldStep
from odepy import dSpaceCollide
from odepy import dNearCallback

from odepy import dMass
from odepy import dMassSetZero
from odepy import dMassSetSphereTotal

from odepy import dBodyCreate
from odepy import dBodySetMass
from odepy import dBodySetPosition
from odepy import dBodyGetPosition

from odepy import dCreateSphere
from odepy import dGeomSetBody
from odepy import dGeomGetBody
from odepy import dGeomSphereGetRadius

from odepy import dJointGroupEmpty
from odepy import dJointCreateContact
from odepy import dJointAttach
from odepy import dContact
from odepy import dCollide
from odepy import dContactBounce

class NearCallbackTestSpace(object):

    def __init__(self, world, contactgroup, groundGeom, ballGeom):
        self.__world = world
        self.__contactgroup = contactgroup
        self.__groundGeom = groundGeom
        self.__ballGeom = ballGeom
        self.__count = 0
        self.__isError = False

    def GetCount(self):
        return self.__count

    def IsError(self):
        return self.__isError

    def Callback(self, data, o1, o2):
        o1IsGround = addressof(self.__groundGeom.contents) == addressof(o1.contents)
        o2IsGround = addressof(self.__groundGeom.contents) == addressof(o2.contents)
        if not (o1IsGround or o2IsGround):
            return

        o1IsBall = addressof(self.__ballGeom.contents) == addressof(o1.contents)
        o2IsBall = addressof(self.__ballGeom.contents) == addressof(o2.contents)
        if not (o1IsBall or o2IsBall):
            return

        self.__count += 1

        ballGeom = o1 if o1IsBall else o2
        ballBody = dGeomGetBody(ballGeom)
        r = dGeomSphereGetRadius(ballGeom)
        z = dBodyGetPosition(ballBody)[2]
        if not (0 <= z and z <= r):
            self.__isError = True
            return

        N = 10
        contacts = (dContact * N)()
        n = dCollide(o1, o2, N, byref(contacts[0].geom), sizeof(dContact))
        if not n == 1:
            self.__isError = True
            return

        contact = contacts[0]
        contact.surface.mu = float('inf')
        contact.surface.mode = dContactBounce
        contact.surface.bounce = 0.95
        contact.surface.bounce_vel = 0.0
        c = dJointCreateContact(self.__world, self.__contactgroup, byref(contact))
        dJointAttach(c, dGeomGetBody(contact.geom.g1), dGeomGetBody(contact.geom.g2))

class TestSpace(object):

    debug = False

    @fixture
    def ball(self, world, space):
        m = 1.0
        r = 0.1
        mass = dMass()
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        body = dBodyCreate(world)
        dBodySetMass(body, byref(mass))
        geom = dCreateSphere(space, r)
        dGeomSetBody(geom, body)
        ball = {'body': body, 'geom': geom}
        return ball

    def test_bounce(self, world, space, ground, ball, contactgroup):
        nearCallback = NearCallbackTestSpace(world=world, contactgroup=contactgroup, groundGeom=ground, ballGeom=ball['geom'])
        tDelta = 0.01
        z0 = 3.0
        dBodySetPosition(ball['body'], 0, 0, z0)

        if self.debug:
            from .utils.drawstuff import Drawstuff
            Drawstuff(world=world, geoms=[ball['geom']], space=space, contactgroup=contactgroup, nearCallback=nearCallback.Callback).Run()

        for i in range(999):
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            assert(dWorldStep(world, tDelta) == 1)
            dJointGroupEmpty(contactgroup)
        assert(nearCallback.GetCount() > 0)
        assert(not nearCallback.IsError())
