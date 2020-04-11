# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dMatrix4
from .common import dReal
from .common import dTriIndex
from .common import dGeomID
from .common import dSpaceID
from .common import dVector3

from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_int32
from ctypes import c_void_p
from ctypes import c_uint8

class dxTriMeshData(Structure):
    pass

dTriMeshDataID = POINTER(dxTriMeshData)

dMTV__MIN = 0
dMTV_FIRST = 0
dMTV_SECOND = 1
dMTV_THIRD = 2
dMTV__MAX = 3

dGeomTriMeshDataCreate = loadOde('dGeomTriMeshDataCreate', dTriMeshDataID)
dGeomTriMeshDataDestroy = loadOde('dGeomTriMeshDataDestroy', None, dTriMeshDataID)
dGeomTriMeshDataSet = loadOde('dGeomTriMeshDataSet', None, dTriMeshDataID, c_int32, c_void_p)
dGeomTriMeshSetLastTransform = loadOde('dGeomTriMeshSetLastTransform', None, dGeomID, dMatrix4)
dGeomTriMeshGetLastTransform = loadOde('dGeomTriMeshGetLastTransform', POINTER(dReal), dGeomID)
dGeomTriMeshDataBuildSingle = loadOde('dGeomTriMeshDataBuildSingle', None, dTriMeshDataID,
                                      c_void_p, c_int32, c_int32,
                                      c_void_p, c_int32, c_int32)
dGeomTriMeshDataBuildSingle1 = loadOde('dGeomTriMeshDataBuildSingle1', None, dTriMeshDataID,
                                       c_void_p, c_int32, c_int32,
                                       c_void_p, c_int32, c_int32,
                                       c_void_p)
dGeomTriMeshDataBuildDouble = loadOde('dGeomTriMeshDataBuildDouble', None, dTriMeshDataID,
                                      c_void_p, c_int32, c_int32,
                                      c_void_p, c_int32, c_int32)
dGeomTriMeshDataBuildDouble1 = loadOde('dGeomTriMeshDataBuildDouble1', None, dTriMeshDataID,
                                       c_void_p, c_int32, c_int32,
                                       c_void_p, c_int32, c_int32,
                                       c_void_p)
dGeomTriMeshDataBuildSimple = loadOde('dGeomTriMeshDataBuildSimple', None, dTriMeshDataID,
                                      POINTER(dReal), c_int32,
                                      POINTER(dTriIndex), c_int32)
dGeomTriMeshDataBuildSimple1 = loadOde('dGeomTriMeshDataBuildSimple1', None, dTriMeshDataID,
                                       POINTER(dReal), c_int32,
                                       POINTER(dTriIndex), c_int32,
                                       POINTER(c_int32))
dGeomTriMeshDataPreprocess = loadOde('dGeomTriMeshDataPreprocess', c_int32, dTriMeshDataID)
dGeomTriMeshDataGetBuffer = loadOde('dGeomTriMeshDataGetBuffer', None, dTriMeshDataID, POINTER(POINTER(c_uint8)), POINTER(c_int32))
dGeomTriMeshDataSetBuffer = loadOde('dGeomTriMeshDataSetBuffer', None, dTriMeshDataID, POINTER(POINTER(c_uint8)))
dTriCallback = CFUNCTYPE(c_int32, dGeomID, dGeomID, c_int32)
dGeomTriMeshSetCallback = loadOde('dGeomTriMeshSetCallback', None, dGeomID, dTriCallback)
dGeomTriMeshGetCallback = loadOde('dGeomTriMeshGetCallback', dTriCallback, dGeomID)
dTriArrayCallback = CFUNCTYPE(None, dGeomID, dGeomID, POINTER(c_int32), c_int32)
dGeomTriMeshSetArrayCallback = loadOde('dGeomTriMeshSetArrayCallback', None, dGeomID, dTriArrayCallback)
dGeomTriMeshGetArrayCallback = loadOde('dGeomTriMeshGetArrayCallback', dTriArrayCallback, dGeomID)
dTriRayCallback = CFUNCTYPE(c_int32, dGeomID, dGeomID, c_int32, dReal, dReal)
dGeomTriMeshSetRayCallback = loadOde('dGeomTriMeshSetRayCallback', None, dGeomID, dTriRayCallback)
dGeomTriMeshGetRayCallback = loadOde('dGeomTriMeshGetRayCallback', dTriRayCallback, dGeomID)
dTriTriMergeCallback = CFUNCTYPE(c_int32, dGeomID, c_int32, c_int32)
dGeomTriMeshSetTriMergeCallback = loadOde('dGeomTriMeshSetTriMergeCallback', None, dGeomID, dTriTriMergeCallback)
dGeomTriMeshGetTriMergeCallback = loadOde('dGeomTriMeshGetTriMergeCallback', dTriTriMergeCallback, dGeomID)
dCreateTriMesh = loadOde('dCreateTriMesh', dGeomID, dSpaceID, dTriMeshDataID, dTriCallback, dTriArrayCallback, dTriRayCallback)
dGeomTriMeshSetData = loadOde('dGeomTriMeshSetData', None, dGeomID, dTriMeshDataID)
dGeomTriMeshEnableTC = loadOde('dGeomTriMeshEnableTC', None, dGeomID, c_int32, c_int32)
dGeomTriMeshIsTCEnabled = loadOde('dGeomTriMeshIsTCEnabled', c_int32, dGeomID, c_int32)
dGeomTriMeshClearTCCache = loadOde('dGeomTriMeshClearTCCache', None, dGeomID)
dGeomTriMeshGetTriMeshDataID = loadOde('dGeomTriMeshGetTriMeshDataID', dTriMeshDataID, dGeomID)
dGeomTriMeshGetTriangle = loadOde('dGeomTriMeshGetTriangle', None, dGeomID, c_int32, POINTER(dVector3), POINTER(dVector3), POINTER(dVector3))
dGeomTriMeshGetPoint = loadOde('dGeomTriMeshGetPoint', None, dGeomID, c_int32, dReal, dReal, dVector3)
dGeomTriMeshGetTriangleCount = loadOde('dGeomTriMeshGetTriangleCount', c_int32, dGeomID)
dGeomTriMeshDataUpdate = loadOde('dGeomTriMeshDataUpdate', None, dTriMeshDataID)
