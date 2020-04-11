# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dGeomID
from .common import dSpaceID
from .common import dVector3

from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_void_p
from ctypes import c_int32

dNearCallback = CFUNCTYPE(None, c_void_p, dGeomID, dGeomID)

def dSimpleSpaceCreate(space):
    if isinstance(space, int):
        return loadOde('dSimpleSpaceCreate', dSpaceID, c_int32)(space)
    else:
        return loadOde('dSimpleSpaceCreate', dSpaceID, dSpaceID)(space)

def dHashSpaceCreate(space):
    if isinstance(space, int):
        return loadOde('dHashSpaceCreate', dSpaceID, c_int32)(space)
    else:
        return loadOde('dHashSpaceCreate', dSpaceID, dSpaceID)(space)

dQuadTreeSpaceCreate = loadOde('dQuadTreeSpaceCreate', dSpaceID, dSpaceID, dVector3, dVector3, c_int32)
dSweepAndPruneSpaceCreate = loadOde('dSweepAndPruneSpaceCreate', dSpaceID, dSpaceID, c_int32)
dSpaceDestroy = loadOde('dSpaceDestroy', None, dSpaceID)
dHashSpaceSetLevels = loadOde('dHashSpaceSetLevels', None, dSpaceID, c_int32, c_int32)
dHashSpaceGetLevels = loadOde('dHashSpaceGetLevels', None, dSpaceID, POINTER(c_int32), POINTER(c_int32))
dSpaceSetCleanup = loadOde('dSpaceSetCleanup', None, dSpaceID, c_int32)
dSpaceGetCleanup = loadOde('dSpaceGetCleanup', c_int32, dSpaceID)
dSpaceSetSublevel = loadOde('dSpaceSetSublevel', None, dSpaceID, c_int32)
dSpaceGetSublevel = loadOde('dSpaceGetSublevel', c_int32, dSpaceID)
dSpaceSetManualCleanup = loadOde('dSpaceSetManualCleanup', None, dSpaceID, c_int32)
dSpaceGetManualCleanup = loadOde('dSpaceGetManualCleanup', c_int32, dSpaceID)
dSpaceAdd = loadOde('dSpaceAdd', None, dSpaceID, dGeomID)
dSpaceRemove = loadOde('dSpaceRemove', None, dSpaceID, dGeomID)
dSpaceQuery = loadOde('dSpaceQuery', c_int32, dSpaceID, dGeomID)
dSpaceClean = loadOde('dSpaceClean', None, dSpaceID)
dSpaceGetNumGeoms = loadOde('dSpaceGetNumGeoms', c_int32, dSpaceID)
dSpaceGetGeom = loadOde('dSpaceGetGeom', dGeomID, dSpaceID, c_int32)
dSpaceGetClass = loadOde('dSpaceGetClass', c_int32, dSpaceID)
