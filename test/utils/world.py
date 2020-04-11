# -*- coding: utf-8 -*-

from pytest import fixture

from odepy import dInitODE
from odepy import dCloseODE
from odepy import dWorldCreate
from odepy import dWorldSetGravity
from odepy import dWorldDestroy

@fixture
def g():
    return 9.80665

@fixture
def world(g):
    dInitODE()
    world = dWorldCreate()
    dWorldSetGravity(world, 0, 0, -g)
    yield world
    dWorldDestroy(world)
    dCloseODE()
