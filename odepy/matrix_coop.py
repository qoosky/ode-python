# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal
from .cooperative import dResourceContainerID
from .cooperative import dResourceRequirementsID

from ctypes import POINTER
from ctypes import c_uint32

dEstimateCooperativelyFactorLDLTResourceRequirements = loadOde('dEstimateCooperativelyFactorLDLTResourceRequirements', None, dResourceRequirementsID, c_uint32, c_uint32)
dCooperativelyFactorLDLT = loadOde('dCooperativelyFactorLDLT', None, dResourceContainerID, c_uint32, POINTER(dReal), POINTER(dReal), c_uint32, c_uint32)
dEstimateCooperativelySolveLDLTResourceRequirements = loadOde('dEstimateCooperativelySolveLDLTResourceRequirements', None, dResourceRequirementsID, c_uint32, c_uint32)
dCooperativelySolveLDLT = loadOde('dCooperativelySolveLDLT', None, dResourceContainerID, c_uint32, POINTER(dReal), POINTER(dReal), POINTER(dReal), c_uint32, c_uint32)
dEstimateCooperativelySolveL1StraightResourceRequirements = loadOde('dEstimateCooperativelySolveL1StraightResourceRequirements', None, dResourceRequirementsID, c_uint32, c_uint32)
dCooperativelySolveL1Straight = loadOde('dCooperativelySolveL1Straight', None, dResourceContainerID, c_uint32, POINTER(dReal), POINTER(dReal), c_uint32, c_uint32)
dEstimateCooperativelySolveL1TransposedResourceRequirements = loadOde('dEstimateCooperativelySolveL1TransposedResourceRequirements', None, dResourceRequirementsID, c_uint32, c_uint32)
dCooperativelySolveL1Transposed = loadOde('dCooperativelySolveL1Transposed', None, dResourceContainerID, c_uint32, POINTER(dReal), POINTER(dReal), c_uint32, c_uint32)
dEstimateCooperativelyScaleVectorResourceRequirements = loadOde('dEstimateCooperativelyScaleVectorResourceRequirements', None, dResourceRequirementsID, c_uint32, c_uint32)
dCooperativelyScaleVector = loadOde('dCooperativelyScaleVector', None, dResourceContainerID, c_uint32, POINTER(dReal), POINTER(dReal), c_uint32)
