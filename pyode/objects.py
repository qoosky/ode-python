# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal
from .common import dWorldID
from .common import dBodyID

from ctypes import POINTER
from ctypes import c_void_p
from ctypes import c_int32

dWorldCreate = loadOde('dWorldCreate', dWorldID)
dWorldSetGravity = loadOde('dWorldSetGravity', c_void_p, dWorldID, dReal, dReal, dReal)
dWorldStep = loadOde('dWorldStep', c_int32, dWorldID, dReal)
dBodyGetPosition = loadOde('dBodyGetPosition', POINTER(dReal), dBodyID)
dBodyCreate = loadOde('dBodyCreate', dBodyID, dWorldID)
