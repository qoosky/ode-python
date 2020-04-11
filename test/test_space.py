# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref
from ctypes import addressof

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

class NearCallback(object):

    def __init__(self, ground):
        self.__count = 0
        self.__ground = ground

    def GetCount(self):
        return self.__count

    def Callback(self, data, o1, o2):
        self.__count += 1
        o1IsGround = addressof(self.__ground.contents) == addressof(o1.contents)
        o2IsGround = addressof(self.__ground.contents) == addressof(o2.contents)
        assert(o1IsGround or o2IsGround)

class TestSpace(object):

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

    def test_collision(self, world, space, ground, ball):
        nearCallback = NearCallback(ground=ground)
        tDelta = 0.01
        x0 = 0.0
        y0 = 0.0
        z0 = 3.0
        dBodySetPosition(ball['body'], x0, y0, z0)
        for i in range(99):
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            assert(dWorldStep(world, tDelta) == 1)
        assert(nearCallback.GetCount() > 0)
