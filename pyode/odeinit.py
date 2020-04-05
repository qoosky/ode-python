# -*- coding: utf-8 -*-

from .common import loadOde
from ctypes import c_void_p

dInitODE = loadOde('dInitODE', c_void_p)
