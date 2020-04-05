# -*- coding: utf-8 -*-

from pytest import fixture

from pyode import dInitODE
from pyode import dWorldCreate
from pyode import dWorldSetGravity

class TestWorld(object):

    @fixture
    def world(self):
        dInitODE()
        yield dWorldCreate()

    def test_createbody(self, world):
        dWorldSetGravity(world, 0, 0, -0.2)
        assert True
