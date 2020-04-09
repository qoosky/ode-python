# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import c_int32
from ctypes import c_uint32

dInitODE = loadOde('dInitODE', None)
dInitODE2 = loadOde('dInitODE2', c_int32, c_uint32)
dAllocateODEDataForThread = loadOde('dAllocateODEDataForThread', c_int32, c_uint32)
dCleanupODEAllDataForThread = loadOde('dCleanupODEAllDataForThread', None)
dCloseODE = loadOde('dCloseODE', None)
