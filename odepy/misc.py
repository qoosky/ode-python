# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal

from ctypes import POINTER
from ctypes import c_int32
from ctypes import c_ulong

dTestRand = loadOde('dTestRand', c_int32)
dRand = loadOde('dRand', c_ulong)
dRandGetSeed = loadOde('dRandGetSeed', c_ulong)
dRandSetSeed = loadOde('dRandSetSeed', None, c_ulong)
dRandInt = loadOde('dRandInt', c_int32, c_int32)
dRandReal = loadOde('dRandReal', dReal)
dMakeRandomVector = loadOde('dMakeRandomVector', None, POINTER(dReal), c_int32, dReal)
dMakeRandomMatrix = loadOde('dMakeRandomMatrix', None, POINTER(dReal), c_int32, c_int32, dReal)
dClearUpperTriangle = loadOde('dClearUpperTriangle', None, POINTER(dReal), c_int32)
dMaxDifference = loadOde('dMaxDifference', dReal, POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dMaxDifferenceLowerTriangle = loadOde('dMaxDifferenceLowerTriangle', dReal, POINTER(dReal), POINTER(dReal), c_int32)
dPrintMatrix = loadOde('dPrintMatrix', POINTER(dReal), c_int32, c_int32)
