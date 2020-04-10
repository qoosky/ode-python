# -*- coding: utf-8 -*-

from .common import loadOde

from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_int32
from ctypes import c_char

dMessageFunction = CFUNCTYPE(None, c_int32, POINTER(c_char))

dSetErrorHandler = loadOde('dSetErrorHandler', None, POINTER(dMessageFunction))
dSetDebugHandler = loadOde('dSetDebugHandler', None, POINTER(dMessageFunction))
dSetMessageHandler = loadOde('dSetMessageHandler', None, POINTER(dMessageFunction))

dGetErrorHandler = loadOde('dGetErrorHandler', POINTER(dMessageFunction))
dGetDebugHandler = loadOde('dGetDebugHandler', POINTER(dMessageFunction))
dGetMessageHandler = loadOde('dGetMessageHandler', POINTER(dMessageFunction))

dError = loadOde('dError', None, c_int32, POINTER(c_char))
dDebug = loadOde('dDebug', None, c_int32, POINTER(c_char))
dMessage = loadOde('dMessage', None, c_int32, POINTER(c_char))
