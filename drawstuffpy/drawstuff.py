# -*- coding: utf-8 -*-

from ctypes.util import find_library
from ctypes import CDLL
from ctypes import CFUNCTYPE
from functools import partial

from os import path
from os import pathsep
from os import environ

from ctypes import Structure
from ctypes import POINTER
from ctypes import c_float
from ctypes import c_double
from ctypes import c_char
from ctypes import c_uint32
from ctypes import c_int32

class DrawstuffPyError(Exception):
    pass

def __GetDrawstuffLib():
    ldLibraryPath = environ.get('LD_LIBRARY_PATH')
    if ldLibraryPath is None:
        ldLibraryPath = []
    else:
        ldLibraryPath = ldLibraryPath.split(pathsep)
    localOdeInstallLibDir = path.join(environ.get('HOME'), '.odepy', 'lib')
    ldLibraryPath.append(localOdeInstallLibDir)
    environ['LD_LIBRARY_PATH'] = pathsep.join(ldLibraryPath)
    environ['LIBRARY_PATH'] = pathsep.join(ldLibraryPath)
    drawstuffLibName = find_library('drawstuff')
    if drawstuffLibName is None:
        raise DrawstuffPyError('drawstuff library not found.')
    if path.exists(path.join(localOdeInstallLibDir, drawstuffLibName)):
        return CDLL(path.join(localOdeInstallLibDir, drawstuffLibName), use_errno=True)
    return CDLL(drawstuffLibName, use_errno=True)

def __load(lib, name, restype, *args):
    try:
        return (CFUNCTYPE(restype, *args))((name, lib))
    except AttributeError as e:
        print('{} is not available for the installed drawstuff: {}'.format(name, str(e)))
        return None

loadDrawstuff = partial(__load, __GetDrawstuffLib())

DS_NONE = 0
DS_WOOD = 1
DS_CHECKERED = 2
DS_GROUND = 3
DS_SKY = 4

dsStartCallback = CFUNCTYPE(None)
dsStepCallback = CFUNCTYPE(None, c_int32)
dsCommandCallback = CFUNCTYPE(None, c_int32)
dsStopCallback = CFUNCTYPE(None)

class dsFunctions(Structure):

    _fields_ = [('version', c_int32),
                ('start', dsStartCallback),
                ('step', dsStepCallback),
                ('command', dsCommandCallback),
                ('stop', dsStopCallback),
                ('path_to_textures', POINTER(c_char))]

    def _init_(self, version, start, step, command, stop):
        self.version = version
        self.start = start
        self.step = step
        self.command = command
        self.stop = stop

dsSimulationLoop = loadDrawstuff('dsSimulationLoop', None, c_int32, POINTER(POINTER(c_char)), c_int32, c_int32, POINTER(dsFunctions))
dsError = loadDrawstuff('dsError', None, POINTER(c_char))
dsDebug = loadDrawstuff('dsDebug', None, POINTER(c_char))
dsPrint = loadDrawstuff('dsPrint', None, POINTER(c_char))
dsSetViewpoint = loadDrawstuff('dsSetViewpoint', None, POINTER(c_float), POINTER(c_float))
dsGetViewpoint = loadDrawstuff('dsGetViewpoint', None, POINTER(c_float), POINTER(c_float))
dsStop = loadDrawstuff('dsStop', None)
dsElapsedTime = loadDrawstuff('dsElapsedTime', c_double)
dsSetTexture = loadDrawstuff('dsSetTexture', None, c_int32)
dsSetColor = loadDrawstuff('dsSetColor', None, c_float, c_float, c_float)
dsSetColorAlpha = loadDrawstuff('dsSetColorAlpha', None, c_float, c_float, c_float, c_float)
dsDrawBox = loadDrawstuff('dsDrawBox', None, POINTER(c_float), POINTER(c_float), POINTER(c_float))
dsDrawSphere = loadDrawstuff('dsDrawSphere', None, POINTER(c_float), POINTER(c_float), c_float)
dsDrawTriangle = loadDrawstuff('dsDrawTriangle', None, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int32)
dsDrawTriangles = loadDrawstuff('dsDrawTriangles', None, POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int32, c_int32)
dsDrawCylinder = loadDrawstuff('dsDrawCylinder', None, POINTER(c_float), POINTER(c_float), c_float, c_float)
dsDrawCapsule = loadDrawstuff('dsDrawCapsule', None, POINTER(c_float), POINTER(c_float), c_float, c_float)
dsDrawLine = loadDrawstuff('dsDrawLine', None, POINTER(c_float), POINTER(c_float))
dsDrawConvex = loadDrawstuff('dsDrawConvex', None, POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint32, POINTER(c_float), c_uint32, POINTER(c_uint32))
dsDrawBoxD = loadDrawstuff('dsDrawBoxD', None, POINTER(c_double), POINTER(c_double), POINTER(c_double))
dsDrawSphereD = loadDrawstuff('dsDrawSphereD', None, POINTER(c_double), POINTER(c_double), c_float)
dsDrawTriangleD = loadDrawstuff('dsDrawTriangleD', None, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int32)
dsDrawTrianglesD = loadDrawstuff('dsDrawTrianglesD', None, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int32, c_int32)
dsDrawCylinderD = loadDrawstuff('dsDrawCylinderD', None, POINTER(c_double), POINTER(c_double), c_float, c_float)
dsDrawCapsuleD = loadDrawstuff('dsDrawCapsuleD', None, POINTER(c_double), POINTER(c_double), c_float, c_float)
dsDrawLineD = loadDrawstuff('dsDrawLineD', None, POINTER(c_double), POINTER(c_double))
dsDrawConvexD = loadDrawstuff('dsDrawConvexD', None, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint32, POINTER(c_double), c_uint32, POINTER(c_uint32))
dsSetSphereQuality = loadDrawstuff('dsSetSphereQuality', None, c_int32)
dsSetCapsuleQuality = loadDrawstuff('dsSetCapsuleQuality', c_int32)
dsSetDrawMode = loadDrawstuff('dsSetDrawMode', None, c_int32)
