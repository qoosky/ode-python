# -*- coding: utf-8 -*-

from pytest import fixture

from ctypes import byref

from odepy import dInitODE
from odepy import dCloseODE
from odepy import dWorldCreate
from odepy import dWorldSetGravity
from odepy import dWorldDestroy
from odepy import dMass
from odepy import dMassSetZero
from odepy import dMassSetSphereTotal
from odepy import dBodyCreate
from odepy import dBodySetMass
from odepy import dHashSpaceCreate
from odepy import dSpaceDestroy

class TestBase(object):

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

    @fixture
    def space(self):
        space = dHashSpaceCreate(0)
        yield space
        dSpaceDestroy(space)
