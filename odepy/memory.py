# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_void_p
from ctypes import c_int32

dAllocFunction = CFUNCTYPE(c_void_p, c_int32)
dReallocFunction = CFUNCTYPE(c_void_p, c_void_p, c_int32, c_int32)
dFreeFunction = CFUNCTYPE(None, c_void_p, c_int32)

dSetAllocHandler = loadOde('dSetAllocHandler', None, POINTER(dAllocFunction))
dSetReallocHandler = loadOde('dSetReallocHandler', None, POINTER(dReallocFunction))
dSetFreeHandler = loadOde('dSetFreeHandler', None, POINTER(dFreeFunction))

dGetAllocHandler = loadOde('dGetAllocHandler', POINTER(dAllocFunction))
dGetReallocHandler = loadOde('dGetReallocHandler', POINTER(dReallocFunction))
dGetFreeHandler = loadOde('dGetFreeHandler', POINTER(dFreeFunction))
dAlloc = loadOde('dAlloc', c_void_p, c_int32)
dRealloc = loadOde('dRealloc', c_void_p, c_void_p, c_int32, c_int32)
dFree = loadOde('dFree', None, c_void_p, c_int32)
