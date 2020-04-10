# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dGeomID
from .common import dBodyID
from .common import dReal
from .common import dMatrix3
from .common import dQuaternion
from .common import dVector3

from ctypes import POINTER

from ctypes import c_void_p
from ctypes import c_int32

dGeomDestroy = loadOde('dGeomDestroy', None, dGeomID)
dGeomSetData = loadOde('dGeomSetData', None, dGeomID, c_void_p)
dGeomGetData = loadOde('dGeomGetData', c_void_p, dGeomID)
dGeomSetBody = loadOde('dGeomSetBody', None, dGeomID, dBodyID)
dGeomGetBody = loadOde('dGeomGetBody', dBodyID, dGeomID)
dGeomSetPosition = loadOde('dGeomSetPosition', None, dGeomID, dReal, dReal, dReal)
dGeomSetRotation = loadOde('dGeomSetRotation', None, dGeomID, dMatrix3)
dGeomSetQuaternion = loadOde('dGeomSetQuaternion', None, dGeomID, dQuaternion)
dGeomGetPosition = loadOde('dGeomGetPosition', POINTER(dReal), dGeomID)
dGeomCopyPosition = loadOde('dGeomCopyPosition', None, dGeomID, dVector3)
dGeomGetRotation = loadOde('dGeomGetRotation', POINTER(dReal), dGeomID)
dGeomCopyRotation = loadOde('dGeomCopyRotation', None, dGeomID, dMatrix3)
dGeomGetQuaternion = loadOde('dGeomGetQuaternion', None, dGeomID, dQuaternion)
dGeomGetAABB = loadOde('dGeomGetAABB', None, dGeomID, POINTER(dReal))
dGeomIsSpace = loadOde('dGeomIsSpace', c_int32, dGeomID)
