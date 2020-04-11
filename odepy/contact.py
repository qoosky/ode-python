# -*- coding: utf-8 -*-

from .common import dVector3
from .common import dReal
from .common import dGeomID

from ctypes import Structure
from ctypes import c_int32

dContactMu2 = 1
dContactAxisDep = 1
dContactFDir1 = 2
dContactBounce = 4
dContactSoftERP = 8
dContactSoftCFM = 16
dContactMotion1 = 32
dContactMotion2 = 64
dContactMotionN = 128
dContactSlip1 = 256
dContactSlip2 = 512
dContactRolling = 1024
dContactApprox0 = 0
dContactApprox1_1 = 4096
dContactApprox1_2 = 8192
dContactApprox1_N = 16384
dContactApprox1 = 28672

class dSurfaceParameters(Structure):

    _fields_ = [('mode', c_int32),
                ('mu', dReal),
                ('mu2', dReal),
                ('rho', dReal),
                ('rho2', dReal),
                ('rhoN', dReal),
                ('bounce', dReal),
                ('bounce_vel', dReal),
                ('soft_erp', dReal),
                ('soft_cfm', dReal),
                ('motion1', dReal),
                ('motion2', dReal),
                ('motionN', dReal),
                ('slip1', dReal),
                ('slip2', dReal)]

    def _init_(self, mode, mu, mu2, rho, rho2, rhoN, bounce, bounce_vel, soft_erp, soft_cfm, motion1, motion2, motionN, slip1, slip2):
        self.mode = mode
        self.mu = mu
        self.mu2 = mu2
        self.rho = rho
        self.rho2 = rho2
        self.rhoN = rhoN
        self.bounce = bounce
        self.bounce_vel = bounce_vel
        self.soft_erp = soft_erp
        self.soft_cfm = soft_cfm
        self.motion1 = motion1
        self.motion2 = motion2
        self.motionN = motionN
        self.slip1 = slip1
        self.slip2 = slip2

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

class dContact(Structure):

    _fields_ = [('surface', dSurfaceParameters),
                ('geom', dContactGeom),
                ('fdir1', dVector3)]

    def _init_(self, surface, geom, fdir1):
        self.surface = surface
        self.geom = geom
        self.fdir1 = fdir1
