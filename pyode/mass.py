# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dReal
from .common import dGeomID
from .common import dVector3
from .common import dMatrix3

from ctypes import Structure
from ctypes import POINTER

from ctypes import c_void_p
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
dMassSetZero = loadOde('dMassSetZero', c_void_p, POINTER(dMass))

dMassSetParameters = loadOde('dMassSetParameters', c_void_p, POINTER(dReal), dReal, 
                             dReal, dReal, dReal,
                             dReal, dReal, dReal,
                             dReal, dReal, dReal)

dMassSetSphere = loadOde('dMassSetSphere', c_void_p, POINTER(dMass), dReal, dReal)
dMassSetSphereTotal = loadOde('dMassSetSphereTotal', c_void_p, POINTER(dMass), dReal, dReal)
dMassSetCapsule = loadOde('dMassSetCapsule', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCapsuleTotal = loadOde('dMassSetCapsuleTotal', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCylinder = loadOde('dMassSetCylinder', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCylinderTotal = loadOde('dMassSetCylinderTotal', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetBox = loadOde('dMassSetBox', c_void_p, POINTER(dMass), dReal, dReal, dReal, dReal)
dMassSetBoxTotal = loadOde('dMassSetBoxTotal', c_void_p, POINTER(dMass), dReal, dReal, dReal, dReal)
dMassSetTrimesh = loadOde('dMassSetTrimesh', c_void_p, POINTER(dMass), dReal, dGeomID)
dMassSetTrimeshTotal = loadOde('dMassSetTrimeshTotal', c_void_p, POINTER(dMass), dReal, dGeomID)
dMassAdjust = loadOde('dMassAdjust', c_void_p, POINTER(dMass), dReal)
dMassTranslate = loadOde('dMassTranslate', c_void_p, POINTER(dMass), dReal, dReal, dReal)
dMassRotate = loadOde('dMassRotate', c_void_p, POINTER(dMass), dMatrix3)
dMassAdd = loadOde('dMassAdd', c_void_p, POINTER(dMass), POINTER(dMass))
dMassSetCappedCylinder = loadOde('dMassSetCappedCylinder', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
dMassSetCappedCylinderTotal = loadOde('dMassSetCappedCylinderTotal', c_void_p, POINTER(dMass), dReal, c_int32, dReal, dReal)
