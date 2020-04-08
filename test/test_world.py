# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref

from pyode import dInitODE
from pyode import dWorldCreate
from pyode import dWorldSetGravity
from pyode import dMass
from pyode import dMassSetZero
from pyode import dVector3
from pyode import dMatrix3
from pyode import dWorldDestroy
from pyode import dCloseODE
from pyode import dBodyGetPosition
from pyode import dBodyGetRotation
from pyode import dBodyCreate
from pyode import dMassSetSphereTotal
from pyode import dBodySetMass
from pyode import dBodySetPosition
from pyode import dWorldStep

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
        r = 0.2
        m = 1.0
        sphere = dBodyCreate(world)
        mass = dMass()
        dMassSetZero(byref(mass))
        dMassSetSphereTotal(byref(mass), m, r)
        dBodySetMass(sphere, byref(mass))
        return sphere

    def test_world(self, world, sphere):
        dBodySetPosition(sphere, 0.0, 0.0, 2.0)
        for i in range(10):
            dWorldStep(world, 0.01)
            pos = dBodyGetPosition(sphere)
            rot = dBodyGetRotation(sphere)
        assert True
