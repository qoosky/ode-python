# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal

from ctypes import POINTER
from ctypes import c_int32

dSetZero = loadOde('dSetZero', None, POINTER(dReal), c_int32)
dSetValue = loadOde('dSetValue', None, POINTER(dReal), c_int32, dReal)
dDot = loadOde('dDot', dReal, POINTER(dReal), POINTER(dReal), c_int32)
dMultiply0 = loadOde('dMultiply0', None, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_int32, c_int32, c_int32)
dMultiply1 = loadOde('dMultiply1', None, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_int32, c_int32, c_int32)
dMultiply2 = loadOde('dMultiply2', None, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_int32, c_int32, c_int32)
dFactorCholesky = loadOde('dFactorCholesky', c_int32, POINTER(dReal), c_int32)
dSolveCholesky = loadOde('dSolveCholesky', None, POINTER(dReal), POINTER(dReal), c_int32)
dInvertPDMatrix = loadOde('dInvertPDMatrix', c_int32, POINTER(dReal), POINTER(dReal), c_int32)
dIsPositiveDefinite = loadOde('dIsPositiveDefinite', c_int32, POINTER(dReal), c_int32)
dFactorLDLT = loadOde('dFactorLDLT', None, POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dSolveL1 = loadOde('dSolveL1', None, POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dSolveL1T = loadOde('dSolveL1T', None, POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dVectorScale = loadOde('dVectorScale', None, POINTER(dReal), POINTER(dReal), c_int32)
dSolveLDLT = loadOde('dSolveLDLT', None, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dLDLTAddTL = loadOde('dLDLTAddTL', None, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_int32, c_int32)
dLDLTRemove = loadOde('dLDLTRemove', None, POINTER(POINTER(dReal)), POINTER(c_int32), POINTER(dReal), POINTER(dReal),
                      c_int32, c_int32, c_int32, c_int32)
dRemoveRowCol = loadOde('dRemoveRowCol', None, POINTER(dReal), c_int32, c_int32, c_int32)
