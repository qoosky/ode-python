# -*- coding: utf-8 -*-

from .common import loadOde
from .threading import dThreadingFunctionsInfo
from .threading import dThreadingImplementationID

from ctypes import Structure
from ctypes import POINTER

class dxCooperative(Structure):
    pass

class dxResourceRequirements(Structure):
    pass

class dxResourceContainer(Structure):
    pass

dCooperativeID = POINTER(dxCooperative)
dResourceRequirementsID = POINTER(dxResourceRequirements)
dResourceContainerID = POINTER(dxResourceContainer)

dCooperativeCreate = loadOde('dCooperativeCreate', dCooperativeID, POINTER(dThreadingFunctionsInfo), dThreadingImplementationID)
dCooperativeDestroy = loadOde('dCooperativeDestroy', None, dCooperativeID)
dResourceRequirementsCreate = loadOde('dResourceRequirementsCreate', dResourceRequirementsID, dCooperativeID)
dResourceRequirementsDestroy = loadOde('dResourceRequirementsDestroy', None, dResourceRequirementsID)
dResourceRequirementsClone = loadOde('dResourceRequirementsClone', dResourceRequirementsID, dResourceRequirementsID)
dResourceRequirementsMergeIn = loadOde('dResourceRequirementsMergeIn', None, dResourceRequirementsID, dResourceRequirementsID)
dResourceContainerAcquire = loadOde('dResourceContainerAcquire', dResourceContainerID, dResourceRequirementsID)
dResourceContainerDestroy = loadOde('dResourceContainerDestroy', None, dResourceContainerID)
