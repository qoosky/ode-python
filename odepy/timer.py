# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import Structure
from ctypes import POINTER
from ctypes import c_double
from ctypes import c_ulong
from ctypes import c_char

class dStopwatch(Structure):

    _fields_ = [('time', c_double),
                ('cc', POINTER(c_ulong))]

    def _init_(self, time, cc):
        self.time = time
        self.cc = cc

dStopwatchReset = loadOde('dStopwatchReset', None, POINTER(dStopwatch))
dStopwatchStart = loadOde('dStopwatchStart', None, POINTER(dStopwatch))
dStopwatchStop = loadOde('dStopwatchStop', None, POINTER(dStopwatch))
dStopwatchTime = loadOde('dStopwatchTime', c_double, POINTER(dStopwatch))
dTimerStart = loadOde('dTimerStart', None, POINTER(c_char))
dTimerNow = loadOde('dTimerNow', None, POINTER(c_char))
dTimerEnd = loadOde('dTimerEnd', None)
dTimerTicksPerSecond = loadOde('dTimerTicksPerSecond', c_double)
dTimerResolution = loadOde('dTimerResolution', c_double)
