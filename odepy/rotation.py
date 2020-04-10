# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dVector3
from .common import dMatrix3
from .common import dReal
from .common import dQuaternion

from ctypes import POINTER

dRSetIdentity = loadOde('dRSetIdentity', None, dMatrix3)
dRFromAxisAndAngle = loadOde('dRFromAxisAndAngle', None, dMatrix3, dReal, dReal, dReal, dReal)
dRFromEulerAngles = loadOde('dRFromEulerAngles', None, dMatrix3, dReal, dReal, dReal)
dRFrom2Axes = loadOde('dRFrom2Axes', None, dMatrix3, dReal, dReal, dReal, dReal, dReal, dReal)
dRFromZAxis = loadOde('dRFromZAxis', None, dMatrix3, dReal, dReal, dReal)
dQSetIdentity = loadOde('dQSetIdentity', None, dQuaternion)
dQFromAxisAndAngle = loadOde('dQFromAxisAndAngle', None, dQuaternion, dReal, dReal, dReal, dReal)
dQMultiply0 = loadOde('dQMultiply0', None, dQuaternion, dQuaternion, dQuaternion)
dQMultiply1 = loadOde('dQMultiply1', None, dQuaternion, dQuaternion, dQuaternion)
dQMultiply2 = loadOde('dQMultiply2', None, dQuaternion, dQuaternion, dQuaternion)
dQMultiply3 = loadOde('dQMultiply3', None, dQuaternion, dQuaternion, dQuaternion)
dRfromQ = loadOde('dRfromQ', None, dMatrix3, dQuaternion)
dQfromR = loadOde('dQfromR', None, dQuaternion, dMatrix3)
dDQfromW = loadOde('dDQfromW', None, POINTER(dReal), dVector3, dQuaternion)
