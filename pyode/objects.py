# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal
from .common import dWorldID

from ctypes import c_void_p

dWorldCreate = loadOde('dWorldCreate', dWorldID)
dWorldSetGravity = loadOde('dWorldSetGravity', c_void_p, dWorldID, dReal, dReal, dReal)
