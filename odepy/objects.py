# -*- coding: utf-8 -*-

from .common import loadOde

from .common import dReal
from .common import dWorldID
from .common import dBodyID
from .common import dVector3
from .common import dMatrix3
from .common import dQuaternion
from .mass import dMass
from .threading import dThreadingImplementationID
from .threading import dThreadingFunctionsInfo

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
dWorldSetStepThreadingImplementation = loadOde('dWorldSetStepThreadingImplementation', None, dWorldID, POINTER(dThreadingFunctionsInfo), dThreadingImplementationID)
dWorldStep = loadOde('dWorldStep', c_int32, dWorldID, dReal)
dWorldQuickStep = loadOde('dWorldQuickStep', c_int32, dWorldID, dReal)
dWorldImpulseToForce = loadOde('dWorldImpulseToForce', None, dWorldID, dReal, dReal, dReal, dReal, dVector3)
dWorldSetQuickStepNumIterations = loadOde('dWorldSetQuickStepNumIterations', None, dWorldID, c_int32)
dWorldGetQuickStepNumIterations = loadOde('dWorldGetQuickStepNumIterations', c_int32, dWorldID)
dWorldSetQuickStepW = loadOde('dWorldSetQuickStepW', None, dWorldID, dReal)
dWorldGetQuickStepW = loadOde('dWorldGetQuickStepW', dReal, dWorldID)
dWorldSetContactMaxCorrectingVel = loadOde('dWorldSetContactMaxCorrectingVel', None, dWorldID, dReal)
dWorldGetContactMaxCorrectingVel = loadOde('dWorldGetContactMaxCorrectingVel', dReal, dWorldID)
dWorldSetContactSurfaceLayer = loadOde('dWorldSetContactSurfaceLayer', None, dWorldID, dReal)
dWorldGetContactSurfaceLayer = loadOde('dWorldGetContactSurfaceLayer', dReal, dWorldID)
dWorldGetAutoDisableLinearThreshold = loadOde('dWorldGetAutoDisableLinearThreshold', dReal, dWorldID)
dWorldSetAutoDisableLinearThreshold = loadOde('dWorldSetAutoDisableLinearThreshold', None, dWorldID, dReal)
dWorldGetAutoDisableAngularThreshold = loadOde('dWorldGetAutoDisableAngularThreshold', dReal, dWorldID)
dWorldSetAutoDisableAngularThreshold = loadOde('dWorldSetAutoDisableAngularThreshold', None, dWorldID, dReal)
dWorldGetAutoDisableAverageSamplesCount = loadOde('dWorldGetAutoDisableAverageSamplesCount', c_int32, dWorldID)
dWorldSetAutoDisableAverageSamplesCount = loadOde('dWorldSetAutoDisableAverageSamplesCount', None, dWorldID, c_uint32)
dWorldGetAutoDisableSteps = loadOde('dWorldGetAutoDisableSteps', c_int32, dWorldID)
dWorldSetAutoDisableSteps = loadOde('dWorldSetAutoDisableSteps', None, dWorldID, c_int32)
dWorldGetAutoDisableTime = loadOde('dWorldGetAutoDisableTime', dReal, dWorldID)
dWorldSetAutoDisableTime = loadOde('dWorldSetAutoDisableTime', None, dWorldID, dReal)
dWorldGetAutoDisableFlag = loadOde('dWorldGetAutoDisableFlag', c_int32, dWorldID)
dWorldSetAutoDisableFlag = loadOde('dWorldSetAutoDisableFlag', None, dWorldID, c_int32)
dWorldGetLinearDampingThreshold = loadOde('dWorldGetLinearDampingThreshold', dReal, dWorldID)
dWorldSetLinearDampingThreshold = loadOde('dWorldSetLinearDampingThreshold', None, dWorldID, dReal)
dWorldGetAngularDampingThreshold = loadOde('dWorldGetAngularDampingThreshold', dReal, dWorldID)
dWorldSetAngularDampingThreshold = loadOde('dWorldSetAngularDampingThreshold', None, dWorldID, dReal)
dWorldGetLinearDamping = loadOde('dWorldGetLinearDamping', dReal, dWorldID)
dWorldSetLinearDamping = loadOde('dWorldSetLinearDamping', None, dWorldID, dReal)
dWorldGetAngularDamping = loadOde('dWorldGetAngularDamping', dReal, dWorldID)
dWorldSetAngularDamping = loadOde('dWorldSetAngularDamping', None, dWorldID, dReal)
dWorldSetDamping = loadOde('dWorldSetDamping', None, dWorldID, dReal, dReal)
dWorldGetMaxAngularSpeed = loadOde('dWorldGetMaxAngularSpeed', dReal, dWorldID)
dWorldSetMaxAngularSpeed = loadOde('dWorldSetMaxAngularSpeed', None, dWorldID, dReal)
dBodyGetAutoDisableLinearThreshold = loadOde('dBodyGetAutoDisableLinearThreshold', dReal, dBodyID)
dBodySetAutoDisableLinearThreshold = loadOde('dBodySetAutoDisableLinearThreshold', None, dBodyID, dReal)
dBodyGetAutoDisableAngularThreshold = loadOde('dBodyGetAutoDisableAngularThreshold', dReal, dBodyID)
dBodySetAutoDisableAngularThreshold = loadOde('dBodySetAutoDisableAngularThreshold', None, dBodyID, dReal)
dBodyGetAutoDisableAverageSamplesCount = loadOde('dBodyGetAutoDisableAverageSamplesCount', c_int32, dBodyID)
dBodySetAutoDisableAverageSamplesCount = loadOde('dBodySetAutoDisableAverageSamplesCount', None, dBodyID, c_uint32)
dBodyGetAutoDisableSteps = loadOde('dBodyGetAutoDisableSteps', c_int32, dBodyID)
dBodySetAutoDisableSteps = loadOde('dBodySetAutoDisableSteps', None, dBodyID, c_int32)
dBodyGetAutoDisableTime = loadOde('dBodyGetAutoDisableTime', dReal, dBodyID)
dBodySetAutoDisableTime = loadOde('dBodySetAutoDisableTime', None, dBodyID, dReal)
dBodyGetAutoDisableFlag = loadOde('dBodyGetAutoDisableFlag', c_int32, dBodyID)
dBodySetAutoDisableFlag = loadOde('dBodySetAutoDisableFlag', None, dBodyID, c_int32)
dBodySetAutoDisableDefaults = loadOde('dBodySetAutoDisableDefaults', None, dBodyID)
dBodyGetWorld = loadOde('dBodyGetWorld', dWorldID, dBodyID)
dBodyCreate = loadOde('dBodyCreate', dBodyID, dWorldID)
dBodyDestroy = loadOde('dBodyDestroy', None, dBodyID)
dBodySetData = loadOde('dBodySetData', None, dBodyID, c_void_p)
dBodyGetData = loadOde('dBodyGetData', c_void_p, dBodyID)
dBodySetPosition = loadOde('dBodySetPosition', None, dBodyID, dReal, dReal, dReal)
dBodySetRotation = loadOde('dBodySetRotation', None, dBodyID, dMatrix3)
dBodySetQuaternion = loadOde('dBodySetQuaternion', None, dBodyID, dQuaternion)
dBodySetLinearVel = loadOde('dBodySetLinearVel', None, dBodyID, dReal, dReal, dReal)
dBodySetAngularVel = loadOde('dBodySetAngularVel', None, dBodyID, dReal, dReal, dReal)
dBodyGetPosition = loadOde('dBodyGetPosition', POINTER(dReal), dBodyID)
dBodyCopyPosition = loadOde('dBodyCopyPosition', None, dBodyID, dVector3)
dBodyGetRotation = loadOde('dBodyGetRotation', POINTER(dReal), dBodyID)
dBodyCopyRotation = loadOde('dBodyCopyRotation', None, dBodyID, dMatrix3)
dBodyGetQuaternion = loadOde('dBodyGetQuaternion', POINTER(dReal), dBodyID)
dBodyCopyQuaternion = loadOde('dBodyCopyQuaternion', None, dBodyID, dQuaternion)
dBodyGetLinearVel = loadOde('dBodyGetLinearVel', POINTER(dReal), dBodyID)


dBodySetMass = loadOde('dBodySetMass', None, dBodyID, POINTER(dMass))
