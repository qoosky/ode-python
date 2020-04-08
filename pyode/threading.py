# -*- coding: utf-8 -*-

from ctypes import Structure
from ctypes import POINTER
from ctypes import c_uint32

class dxThreadingImplementation(Structure):
    pass

dThreadingImplementationID = POINTER(dxThreadingImplementation)

dmutexindex_t = c_uint32

class dxMutexGroup(Structure):
    pass

dMutexGroupID = POINTER(dxMutexGroup)
