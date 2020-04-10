# -*- coding: utf-8 -*-

from .common import dVector3
from .common import dReal
from .common import dGeomID

from ctypes import Structure
from ctypes import c_int32

class dContactGeom(Structure):

    _fields_ = [('pos', dVector3),
                ('normal', dVector3),
                ('depth', dReal),
                ('g1', dGeomID),
                ('g2', dGeomID),
                ('side1', c_int32),
                ('side2', c_int32)]

    def _init_(self, pos, normal, depth, g1, g2, side1, side2):
        self.pos = pos
        self.normal = normal
        self.depth = depth
        self.g1 = g1
        self.g2 = g2
        self.side1 = side1
        self.side2 = side2
