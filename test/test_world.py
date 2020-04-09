# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref

from pyode import dInitODE
from pyode import dCloseODE
from pyode import dWorldCreate
from pyode import dWorldSetGravity
from pyode import dWorldStep
from pyode import dWorldDestroy
from pyode import dVector3
from pyode import dMatrix3
from pyode import dMass
from pyode import dMassSetZero
from pyode import dMassSetSphereTotal
from pyode import dBodyCreate
from pyode import dBodySetMass
from pyode import dBodySetPosition
from pyode import dBodyGetPosition
from pyode import dBodyGetRotation
from pyode import dBodyGetLinearVel

class TestWorld(object):

    @fixture
    def g(self):
        return 9.80665

    @fixture
    def world(self, g):
        dInitODE()
        world = dWorldCreate()
        dWorldSetGravity(world, 0, 0, -g)
        yield world
        dWorldDestroy(world)
        dCloseODE()

    @fixture
    def sphere(self, world):
        r = 0.1
        m = 1.0
        sphere = dBodyCreate(world)
        mass = dMass()
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        dBodySetMass(sphere, byref(mass))
        return sphere

    def test_freefall(self, g, world, sphere):
        z0 = 5.0
        deltaT = 0.01
        eps = 0.05
        dBodySetPosition(sphere, 0.0, 0.0, z0)
        for i in range(99):
            pos = dBodyGetPosition(sphere)
            rot = dBodyGetRotation(sphere)
            vel = dBodyGetLinearVel(sphere)
            t = deltaT * i
            v = -g * t
            z = z0 - (g * t * t / 2.0)
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
            assert(dWorldStep(world, deltaT) == 1)
        assert True
