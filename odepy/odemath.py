# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dVector3
from .common import dVector4
from .common import dMatrix3

from ctypes import c_int32

dSafeNormalize3 = loadOde('dSafeNormalize3', c_int32, dVector3)
dSafeNormalize4 = loadOde('dSafeNormalize4', c_int32, dVector4)
dNormalize3 = loadOde('dNormalize3', None, dVector3)
dNormalize4 = loadOde('dNormalize4', None, dVector4)
dPlaneSpace = loadOde('dPlaneSpace', None, dVector3, dVector3, dVector3)
dOrthogonalizeR = loadOde('dOrthogonalizeR', c_int32, dMatrix3)
