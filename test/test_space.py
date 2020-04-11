# -*- coding: utf-8 -*-

from pytest import fixture
from ctypes import byref
from ctypes import addressof

from odepy import dNearCallback
from odepy import dWorldStep
from odepy import dBodySetPosition
from odepy import dBodyGetPosition
from odepy import dSpaceCollide
from odepy import dBodyCreate
from odepy import dMass
from odepy import dMassSetZero
from odepy import dMassSetSphereTotal
from odepy import dBodySetMass
from odepy import dCreateSphere
from odepy import dGeomSetBody

class NearCallback(object):

    def __init__(self, ground):
        self.__ground = ground

    def Callback(self, data, o1, o2):
        print(addressof(self.__ground.contents) == addressof(o1.contents))
        print(addressof(self.__ground.contents) == addressof(o2.contents))

class TestSpace(object):

    @fixture
    def ball(self, world, space):
        body = dBodyCreate(world)
        mass = dMass()
        dMassSetZero(byref(mass))
        m = 1.0
        r = 0.2
        dMassSetSphereTotal(byref(mass), m, r)
        dBodySetMass(body, byref(mass))
        x0 = 0.0
        y0 = 0.0
        z0 = 2.0
        dBodySetPosition(body, x0, y0, z0)
        geom = dCreateSphere(space, r)
        dGeomSetBody(geom, body)
        ball = {'body': body, 'geom': geom}
        return ball

    def test_collision(self, world, space, ground, ball):
        for i in range(62):
            nearCallback = NearCallback(ground=ground)
            dSpaceCollide(space, 0, dNearCallback(nearCallback.Callback))
            pos = dBodyGetPosition(ball['body'])
            aaa = [pos[i] for i in range(4)]
            print(aaa[2])
            dWorldStep(world, 0.01)
