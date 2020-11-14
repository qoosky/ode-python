# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal
from .common import dGeomID
from .common import dVector3
from .common import dMatrix3

from ctypes import Structure
from ctypes import POINTER

from ctypes import c_int32

class dMass(Structure):

    _fields_ = [('mass', dReal),
                ('c', dVector3),
                ('I', dMatrix3)]

    def _init_(self, mass, c, I):
        self.mass = mass
        self.c = c
        self.I = I

dMassCheck = loadOde('dMassCheck', c_int32, POINTER(dMass))
dMassSetZero = loadOde('dMassSetZero', None, POINTER(dMass))
dMassSetParameters = loadOde('dMassSetParameters', None, POINTER(dMass), dReal,
                             dReal, dReal, dReal,
                             dReal, dReal, dReal,
                             dReal, dReal, dReal)
dMassSetSphere = loadOde('dMassSetSphere', None, POINTER(dMass), dReal, dReal)
dMassSetSphereTotal = loadOde('dMassSetSphereTotal', None, POINTER(dMass), dReal, dReal)
dMassSetCapsule = loadOde('dMassSetCapsule', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCapsuleTotal = loadOde('dMassSetCapsuleTotal', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCylinder = loadOde('dMassSetCylinder', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCylinderTotal = loadOde('dMassSetCylinderTotal', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetBox = loadOde('dMassSetBox', None, POINTER(dMass), dReal, dReal, dReal, dReal)
dMassSetBoxTotal = loadOde('dMassSetBoxTotal', None, POINTER(dMass), dReal, dReal, dReal, dReal)
dMassSetTrimesh = loadOde('dMassSetTrimesh', None, POINTER(dMass), dReal, dGeomID)
dMassSetTrimeshTotal = loadOde('dMassSetTrimeshTotal', None, POINTER(dMass), dReal, dGeomID)
dMassAdjust = loadOde('dMassAdjust', None, POINTER(dMass), dReal)
dMassTranslate = loadOde('dMassTranslate', None, POINTER(dMass), dReal, dReal, dReal)
dMassRotate = loadOde('dMassRotate', None, POINTER(dMass), dMatrix3)
dMassAdd = loadOde('dMassAdd', None, POINTER(dMass), POINTER(dMass))
dMassSetCappedCylinder = loadOde('dMassSetCappedCylinder', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCappedCylinderTotal = loadOde('dMassSetCappedCylinderTotal', None, POINTER(dMass), dReal, c_int32, dReal, dReal)
