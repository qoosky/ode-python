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
from ctypes import c_uint32

def __GetOdeLib():
    odeLibName = find_library('ode')
    if odeLibName is not None:
        odeLib = CDLL(odeLibName, use_errno=True)
    else:
        ldLibraryPath = environ.get('LD_LIBRARY_PATH')
        if ldLibraryPath is None:
            ldLibraryPath = []
        else:
            ldLibraryPath = ldLibraryPath.split(pathsep)
        localOdeInstallLibDir = path.join(environ.get('HOME'), '.pyode', 'lib')
        ldLibraryPath.append(localOdeInstallLibDir)
        environ['LD_LIBRARY_PATH'] = pathsep.join(ldLibraryPath)
        odeLib = CDLL(path.join(localOdeInstallLibDir, find_library('ode')), use_errno=True)
    return odeLib

def __load(lib, name, restype, *args):
    return (CFUNCTYPE(restype, *args))((name, lib))

loadOde = partial(__load, __GetOdeLib())

class dxWorld(Structure):
    pass

class dxSpace(Structure):
    pass

class dxBody(Structure):
    pass

class dxGeom(Structure):
    pass

class dxJoint(Structure):
    pass

class dxJointGroup(Structure):
    pass

dReal = c_float
dTriIndex = c_uint32
dWorldID = POINTER(dxWorld)
dSpaceID = POINTER(dxSpace)
dBodyID = POINTER(dxBody)
dGeomID = POINTER(dxGeom)
dJointID = POINTER(dxJoint)
dJointGroupID = POINTER(dxJointGroup)
