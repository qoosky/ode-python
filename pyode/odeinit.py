# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import c_void_p
from ctypes import c_int32
from ctypes import c_uint32

dInitODE = loadOde('dInitODE', c_void_p)
dInitODE2 = loadOde('dInitODE2', c_int32, c_uint32)
dAllocateODEDataForThread = loadOde('dAllocateODEDataForThread', c_int32, c_uint32)
dCleanupODEAllDataForThread = loadOde('dCleanupODEAllDataForThread', c_void_p)
dCloseODE = loadOde('dCloseODE', c_void_p)
