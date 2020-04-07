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

class TestWorld(object):

    @fixture
    def world(self):
        dInitODE()
        yield dWorldCreate()

    def test_createbody(self, world):
        dWorldSetGravity(world, 0, 0, -0.2)
        mass = dMass()
        dMassSetZero(byref(mass))
        assert True
