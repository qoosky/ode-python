# -*- coding: utf-8 -*-

from pytest import fixture

from odepy import dHashSpaceCreate
from odepy import dSpaceDestroy
from odepy import dCreatePlane
from odepy import dJointGroupCreate

@fixture
def space():
    space = dHashSpaceCreate(0)
    yield space
    dSpaceDestroy(space)

@fixture
def ground(space):
    ground = dCreatePlane(space, 0, 0, 1, 0)
    return ground

@fixture
def contactgroup():
    contactgroup = dJointGroupCreate(0)
    return contactgroup
