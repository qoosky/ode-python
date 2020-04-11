# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import CFUNCTYPE
from ctypes import c_void_p
from ctypes import c_int32

dAllocFunction = CFUNCTYPE(c_void_p, c_int32)
dReallocFunction = CFUNCTYPE(c_void_p, c_void_p, c_int32, c_int32)
dFreeFunction = CFUNCTYPE(None, c_void_p, c_int32)

dSetAllocHandler = loadOde('dSetAllocHandler', None, dAllocFunction)
dSetReallocHandler = loadOde('dSetReallocHandler', None, dReallocFunction)
dSetFreeHandler = loadOde('dSetFreeHandler', None, dFreeFunction)

dGetAllocHandler = loadOde('dGetAllocHandler', dAllocFunction)
dGetReallocHandler = loadOde('dGetReallocHandler', dReallocFunction)
dGetFreeHandler = loadOde('dGetFreeHandler', dFreeFunction)
dAlloc = loadOde('dAlloc', c_void_p, c_int32)
dRealloc = loadOde('dRealloc', c_void_p, c_void_p, c_int32, c_int32)
dFree = loadOde('dFree', None, c_void_p, c_int32)
