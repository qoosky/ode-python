# -*- coding: utf-8 -*-

from pytest import fixture
from ctypes import byref

from odepy import dMass
from odepy import dMassSetZero
from odepy import dMassSetSphereTotal

from odepy import dBodyCreate
from odepy import dBodySetMass

from odepy import dWorldStep
from odepy import dBodySetPosition
from odepy import dBodyGetPosition
from odepy import dBodyGetRotation
from odepy import dBodyGetLinearVel

class TestWorld(object):

    @fixture
    def sphere(self, world):
        r = 0.1
        m = 1.0
        mass = dMass()
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        sphere = dBodyCreate(world)
        dBodySetMass(sphere, byref(mass))
        return sphere

    def test_freefall(self, g, world, sphere):
        z0 = 5.0
        tDelta = 0.01
        eps = 0.05
        dBodySetPosition(sphere, 0.0, 0.0, z0)
        for i in range(99):
            pos = dBodyGetPosition(sphere)
            rot = dBodyGetRotation(sphere)
            vel = dBodyGetLinearVel(sphere)
            t = tDelta * i
            v = g[2] * t
            z = z0 + (g[2] * t * t / 2.0)
            for i in range(3):
                if i < 2:
                    assert(pos[i] == 0)
                    assert(vel[i] == 0)
                else:
                    assert(abs(pos[i] - z) < eps)
                    assert(abs(vel[i] - v) < eps)
            for i in range(3):
                for j in range(4):
                    if i == j:
                        assert(rot[4 * i + j] == 1.0)
                    else:
                        assert(rot[4 * i + j] == 0.0)
            assert(dWorldStep(world, tDelta) == 1)
