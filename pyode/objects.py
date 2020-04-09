# -*- coding: utf-8 -*-

from .common import loadOde

from .common import dReal
from .common import dWorldID
from .common import dBodyID
from .common import dVector3
from pyode import dMass

from ctypes import Structure
from ctypes import POINTER
from ctypes import c_void_p
from ctypes import c_int32
from ctypes import c_uint32
from ctypes import c_float

dWorldCreate = loadOde('dWorldCreate', dWorldID)
dWorldDestroy = loadOde('dWorldDestroy', None, dWorldID)
dWorldSetData = loadOde('dWorldSetData', None, dWorldID, c_void_p)
dWorldGetData = loadOde('dWorldGetData', c_void_p, dWorldID)
dWorldSetGravity = loadOde('dWorldSetGravity', None, dWorldID, dReal, dReal, dReal)
dWorldGetGravity = loadOde('dWorldGetGravity', None, dWorldID, dVector3)
dWorldSetERP = loadOde('dWorldSetERP', None, dWorldID, dReal)
dWorldGetERP = loadOde('dWorldGetERP', dReal, dWorldID)
dWorldSetCFM = loadOde('dWorldSetCFM', None, dWorldID, dReal)
dWorldGetCFM = loadOde('dWorldGetCFM', dReal, dWorldID)
dWorldSetStepIslandsProcessingMaxThreadCount = loadOde('dWorldSetStepIslandsProcessingMaxThreadCount', None, dWorldID, c_uint32)
dWorldGetStepIslandsProcessingMaxThreadCount = loadOde('dWorldGetStepIslandsProcessingMaxThreadCount', c_uint32, dWorldID)
dWorldUseSharedWorkingMemory = loadOde('dWorldUseSharedWorkingMemory', c_int32, dWorldID, dWorldID)
dWorldCleanupWorkingMemory = loadOde('dWorldCleanupWorkingMemory', None, dWorldID)

class dWorldStepReserveInfo(Structure):

    _fields_ = [('struct_size', c_uint32),
                ('reserve_factor', c_float),
                ('reserve_minimum', c_uint32)]

    def _init_(self, struct_size, reserve_factor, reserve_minimum):
        self.struct_size = struct_size
        self.reserve_factor = reserve_factor
        self.reserve_minimum = reserve_minimum

dWorldSetStepMemoryReservationPolicy = loadOde('dWorldSetStepMemoryReservationPolicy', c_int32, dWorldID, POINTER(dWorldStepReserveInfo))
dWorldStep = loadOde('dWorldStep', c_int32, dWorldID, dReal)
dBodyGetPosition = loadOde('dBodyGetPosition', POINTER(dReal), dBodyID)
dBodyCreate = loadOde('dBodyCreate', dBodyID, dWorldID)
dBodyGetRotation = loadOde('dBodyGetRotation', POINTER(dReal), dBodyID)
dBodySetMass = loadOde('dBodySetMass', None, dBodyID, POINTER(dMass))
dBodySetPosition = loadOde('dBodySetPosition', None, dBodyID, dReal, dReal, dReal)
dBodyGetLinearVel = loadOde('dBodyGetLinearVel', POINTER(dReal), dBodyID)
