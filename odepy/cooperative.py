# -*- coding: utf-8 -*-

from .common import loadOde

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
