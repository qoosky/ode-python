# -*- coding: utf-8 -*-

from .common import loadOde
from .common import dGeomID
from .common import dBodyID
from .common import dReal
from .common import dMatrix3
from .common import dQuaternion
from .common import dVector3
from .common import dVector4
from .common import dSpaceID
from .contact import dContactGeom
from .collision_space import dNearCallback

from ctypes import POINTER
from ctypes import Structure
from ctypes import CFUNCTYPE

from ctypes import c_void_p
from ctypes import c_int32
from ctypes import c_uint32
from ctypes import c_ulong
from ctypes import c_uint8
from ctypes import c_uint16
from ctypes import c_float
from ctypes import c_double

dGeomDestroy = loadOde('dGeomDestroy', None, dGeomID)
dGeomSetData = loadOde('dGeomSetData', None, dGeomID, c_void_p)
dGeomGetData = loadOde('dGeomGetData', c_void_p, dGeomID)
dGeomSetBody = loadOde('dGeomSetBody', None, dGeomID, dBodyID)
dGeomGetBody = loadOde('dGeomGetBody', dBodyID, dGeomID)
dGeomSetPosition = loadOde('dGeomSetPosition', None, dGeomID, dReal, dReal, dReal)
dGeomSetRotation = loadOde('dGeomSetRotation', None, dGeomID, dMatrix3)
dGeomSetQuaternion = loadOde('dGeomSetQuaternion', None, dGeomID, dQuaternion)
dGeomGetPosition = loadOde('dGeomGetPosition', POINTER(dReal), dGeomID)
dGeomCopyPosition = loadOde('dGeomCopyPosition', None, dGeomID, dVector3)
dGeomGetRotation = loadOde('dGeomGetRotation', POINTER(dReal), dGeomID)
dGeomCopyRotation = loadOde('dGeomCopyRotation', None, dGeomID, dMatrix3)
dGeomGetQuaternion = loadOde('dGeomGetQuaternion', None, dGeomID, dQuaternion)
dGeomGetAABB = loadOde('dGeomGetAABB', None, dGeomID, POINTER(dReal))
dGeomIsSpace = loadOde('dGeomIsSpace', c_int32, dGeomID)
dGeomGetSpace = loadOde('dGeomGetSpace', dSpaceID, dGeomID)
dGeomGetClass = loadOde('dGeomGetClass', c_int32, dGeomID)
dGeomSetCategoryBits = loadOde('dGeomSetCategoryBits', None, dGeomID, c_ulong)
dGeomSetCollideBits = loadOde('dGeomSetCollideBits', None, dGeomID, c_ulong)
dGeomGetCategoryBits = loadOde('dGeomGetCategoryBits', c_ulong, dGeomID)
dGeomGetCollideBits = loadOde('dGeomGetCollideBits', c_ulong, dGeomID)
dGeomEnable = loadOde('dGeomEnable', None, dGeomID)
dGeomDisable = loadOde('dGeomDisable', None, dGeomID)
dGeomIsEnabled = loadOde('dGeomIsEnabled', c_int32, dGeomID)
dGeomLowLevelControl = loadOde('dGeomLowLevelControl', dGeomID, c_int32, c_int32, c_void_p, POINTER(c_int32))
dGeomGetRelPointPos = loadOde('dGeomGetRelPointPos', None, dGeomID, dReal, dReal, dReal, dVector3)
dGeomGetPosRelPoint = loadOde('dGeomGetPosRelPoint', None, dGeomID, dReal, dReal, dReal, dVector3)
dGeomVectorToWorld = loadOde('dGeomVectorToWorld', None, dGeomID, dReal, dReal, dReal, dVector3)
dGeomVectorFromWorld = loadOde('dGeomVectorFromWorld', None, dGeomID, dReal, dReal, dReal, dVector3)
dGeomSetOffsetPosition = loadOde('dGeomSetOffsetPosition', None, dGeomID, dReal, dReal, dReal)
dGeomSetOffsetRotation = loadOde('dGeomSetOffsetRotation', None, dGeomID, dMatrix3)
dGeomSetOffsetQuaternion = loadOde('dGeomSetOffsetQuaternion', None, dGeomID, dQuaternion)
dGeomSetOffsetWorldPosition = loadOde('dGeomSetOffsetWorldPosition', None, dGeomID, dReal, dReal, dReal)
dGeomSetOffsetWorldRotation = loadOde('dGeomSetOffsetWorldRotation', None, dGeomID, dMatrix3)
dGeomSetOffsetWorldQuaternion = loadOde('dGeomSetOffsetWorldQuaternion', None, dGeomID, dQuaternion)
dGeomClearOffset = loadOde('dGeomClearOffset', None, dGeomID)
dGeomIsOffset = loadOde('dGeomIsOffset', c_int32, dGeomID)
dGeomGetOffsetPosition = loadOde('dGeomGetOffsetPosition', POINTER(dReal), dGeomID)
dGeomCopyOffsetPosition = loadOde('dGeomCopyOffsetPosition', None, dGeomID, dVector3)
dGeomGetOffsetRotation = loadOde('dGeomGetOffsetRotation', POINTER(dReal), dGeomID)
dGeomCopyOffsetRotation = loadOde('dGeomCopyOffsetRotation', None, dGeomID, dMatrix3)
dGeomGetOffsetQuaternion = loadOde('dGeomGetOffsetQuaternion', None, dGeomID, dQuaternion)
dCollide = loadOde('dCollide', c_int32, dGeomID, dGeomID, c_int32, POINTER(dContactGeom), c_int32)
dSpaceCollide = loadOde('dSpaceCollide', None, dSpaceID, c_void_p, dNearCallback)
dSpaceCollide2 = loadOde('dSpaceCollide2', None, dGeomID, dGeomID, c_void_p, dNearCallback)

dSphereClass = 0
dBoxClass = 1
dCapsuleClass = 2
dCylinderClass = 3
dPlaneClass = 4
dRayClass = 5
dConvexClass = 6
dGeomTransformClass = 7
dTriMeshClass = 8
dHeightfieldClass = 9
dFirstSpaceClass = 10
dSimpleSpaceClass = 10
dHashSpaceClass = 11
dSweepAndPruneSpaceClass = 12
dQuadTreeSpaceClass = 13
dLastSpaceClass = 13
dFirstUserClass = 14
dLastUserClass = 17
dGeomNumClasses = 18

dCreateSphere = loadOde('dCreateSphere', dGeomID, dSpaceID, dReal)
dGeomSphereSetRadius = loadOde('dGeomSphereSetRadius', None, dGeomID, dReal)
dGeomSphereGetRadius = loadOde('dGeomSphereGetRadius', dReal, dGeomID)
dGeomSpherePointDepth = loadOde('dGeomSpherePointDepth', dReal, dGeomID, dReal, dReal, dReal)
dCreateConvex = loadOde('dCreateConvex', dGeomID, dSpaceID, POINTER(dReal), c_uint32, POINTER(dReal), c_uint32, POINTER(c_uint32))
dGeomSetConvex = loadOde('dGeomSetConvex', None, dGeomID, POINTER(dReal), c_uint32, POINTER(dReal), c_uint32, POINTER(c_uint32))
dCreateBox = loadOde('dCreateBox', dGeomID, dSpaceID, dReal, dReal, dReal)
dGeomBoxSetLengths = loadOde('dGeomBoxSetLengths', None, dGeomID, dReal, dReal, dReal)
dGeomBoxGetLengths = loadOde('dGeomBoxGetLengths', None, dGeomID, dVector3)
dGeomBoxPointDepth = loadOde('dGeomBoxPointDepth', dReal, dGeomID, dReal, dReal, dReal)
dCreatePlane = loadOde('dCreatePlane', dGeomID, dSpaceID, dReal, dReal, dReal, dReal)
dGeomPlaneSetParams = loadOde('dGeomPlaneSetParams', None, dGeomID, dReal, dReal, dReal, dReal)
dGeomPlaneGetParams = loadOde('dGeomPlaneGetParams', None, dGeomID, dVector4)
dGeomPlanePointDepth = loadOde('dGeomPlanePointDepth', dReal, dGeomID, dReal, dReal, dReal)
dCreateCapsule = loadOde('dCreateCapsule', dGeomID, dSpaceID, dReal, dReal)
dGeomCapsuleSetParams = loadOde('dGeomCapsuleSetParams', None, dGeomID, dReal, dReal)
dGeomCapsuleGetParams = loadOde('dGeomCapsuleGetParams', None, dGeomID, POINTER(dReal), POINTER(dReal))
dGeomCapsulePointDepth = loadOde('dGeomCapsulePointDepth', dReal, dGeomID, dReal, dReal, dReal)
dCreateCylinder = loadOde('dCreateCylinder', dGeomID, dSpaceID, dReal, dReal)
dGeomCylinderSetParams = loadOde('dGeomCylinderSetParams', None, dGeomID, dReal, dReal)
dGeomCylinderGetParams = loadOde('dGeomCylinderGetParams', None, dGeomID, POINTER(dReal), POINTER(dReal))
dCreateRay = loadOde('dCreateRay', dGeomID, dSpaceID, dReal)
dGeomRaySetLength = loadOde('dGeomRaySetLength', None, dGeomID, dReal)
dGeomRayGetLength = loadOde('dGeomRayGetLength', dReal, dGeomID)
dGeomRaySet = loadOde('dGeomRaySet', None, dGeomID, dReal, dReal, dReal, dReal, dReal, dReal)
dGeomRayGet = loadOde('dGeomRayGet', None, dGeomID, dVector3, dVector3)
dGeomRaySetParams = loadOde('dGeomRaySetParams', None, dGeomID, c_int32, c_int32)
dGeomRayGetParams = loadOde('dGeomRayGetParams', None, dGeomID, POINTER(c_int32), POINTER(c_int32))
dGeomRaySetFirstContact = loadOde('dGeomRaySetFirstContact', None, dGeomID, c_int32)
dGeomRayGetFirstContact = loadOde('dGeomRayGetFirstContact', c_int32, dGeomID)
dGeomRaySetBackfaceCull = loadOde('dGeomRaySetBackfaceCull', None, dGeomID, c_int32)
dGeomRayGetBackfaceCull = loadOde('dGeomRayGetBackfaceCull', c_int32, dGeomID)
dGeomRaySetClosestHit = loadOde('dGeomRaySetClosestHit', None, dGeomID, c_int32)
dGeomRayGetClosestHit = loadOde('dGeomRayGetClosestHit', c_int32, dGeomID)
dCreateGeomTransform = loadOde('dCreateGeomTransform', dGeomID, dSpaceID)
dGeomTransformSetGeom = loadOde('dGeomTransformSetGeom', None, dGeomID, dGeomID)
dGeomTransformGetGeom = loadOde('dGeomTransformGetGeom', dGeomID, dGeomID)
dGeomTransformSetCleanup = loadOde('dGeomTransformSetCleanup', None, dGeomID, c_int32)
dGeomTransformGetCleanup = loadOde('dGeomTransformGetCleanup', c_int32, dGeomID)
dGeomTransformSetInfo = loadOde('dGeomTransformSetInfo', None, dGeomID, c_int32)
dGeomTransformGetInfo = loadOde('dGeomTransformGetInfo', c_int32, dGeomID)

class dxHeightfieldData(Structure):
    pass

dHeightfieldDataID = POINTER(dxHeightfieldData)
dHeightfieldGetHeight = CFUNCTYPE(dReal, c_void_p, c_int32, c_int32)
dCreateHeightfield = loadOde('dCreateHeightfield', dGeomID, dSpaceID, dHeightfieldDataID, c_int32)
dGeomHeightfieldDataCreate = loadOde('dGeomHeightfieldDataCreate', dHeightfieldDataID)
dGeomHeightfieldDataDestroy = loadOde('dGeomHeightfieldDataDestroy', None, dHeightfieldDataID)
dGeomHeightfieldDataBuildCallback = loadOde('dGeomHeightfieldDataBuildCallback', None, dHeightfieldDataID,
                                            c_void_p, dHeightfieldGetHeight,
                                            dReal, dReal, c_int32, c_int32,
                                            dReal, dReal, dReal, c_int32)
dGeomHeightfieldDataBuildByte = loadOde('dGeomHeightfieldDataBuildByte', None, dHeightfieldDataID,
                                        POINTER(c_uint8), c_int32,
                                        dReal, dReal, c_int32, c_int32,
                                        dReal, dReal, dReal, c_int32)
dGeomHeightfieldDataBuildShort = loadOde('dGeomHeightfieldDataBuildShort', None, dHeightfieldDataID,
                                         POINTER(c_uint16), c_int32,
                                         dReal, dReal, c_int32, c_int32,
                                         dReal, dReal, dReal, c_int32)
dGeomHeightfieldDataBuildSingle = loadOde('dGeomHeightfieldDataBuildSingle', None, dHeightfieldDataID,
                                          POINTER(c_float), c_int32,
                                          dReal, dReal, c_int32, c_int32,
                                          dReal, dReal, dReal, c_int32)
dGeomHeightfieldDataBuildDouble = loadOde('dGeomHeightfieldDataBuildDouble', None, dHeightfieldDataID,
                                          POINTER(c_double), c_int32,
                                          dReal, dReal, c_int32, c_int32,
                                          dReal, dReal, dReal, c_int32)
dGeomHeightfieldDataSetBounds = loadOde('dGeomHeightfieldDataSetBounds', None, dHeightfieldDataID, dReal, dReal)
dGeomHeightfieldSetHeightfieldData = loadOde('dGeomHeightfieldSetHeightfieldData', None, dGeomID, dHeightfieldDataID)
dGeomHeightfieldGetHeightfieldData = loadOde('dGeomHeightfieldGetHeightfieldData', dHeightfieldDataID, dGeomID)
dClosestLineSegmentPoints = loadOde('dClosestLineSegmentPoints', None, dVector3, dVector3, dVector3, dVector3, dVector3, dVector3)
dBoxTouchesBox = loadOde('dBoxTouchesBox', c_int32, dVector3, dMatrix3, dVector3, dVector3, dMatrix3, dVector3)
dBoxBox = loadOde('dBoxBox', c_int32, dVector3, dMatrix3, dVector3, dVector3, dMatrix3, dVector3,
                  dVector3, POINTER(dReal), POINTER(c_int32),
                  c_int32, POINTER(dContactGeom), c_int32)
dInfiniteAABB = loadOde('dInfiniteAABB', None, dGeomID, POINTER(dReal))
dGetAABBFn = CFUNCTYPE(None, dGeomID, POINTER(dReal))
dColliderFn = CFUNCTYPE(c_int32, dGeomID, dGeomID, c_int32, POINTER(dContactGeom), c_int32)
dGetColliderFnFn = CFUNCTYPE(dColliderFn, c_int32)
dGeomDtorFn = CFUNCTYPE(None, dGeomID)
dAABBTestFn = CFUNCTYPE(c_int32, dGeomID, dGeomID, POINTER(dReal))

class dGeomClass(Structure):

    _fields_ = [('bytes', c_int32),
                ('collider', dGetColliderFnFn),
                ('aabb', dGetAABBFn),
                ('aabb_test', dAABBTestFn),
                ('dtor', dGeomDtorFn)]

    def _init_(self, bytes, collider, aabb, aabb_test, dtor):
        self.bytes = bytes
        self.collider = collider
        self.aabb = aabb
        self.aabb_test = aabb_test
        self.dtor = dtor

dCreateGeomClass = loadOde('dCreateGeomClass', c_int32, POINTER(dGeomClass))
dGeomGetClassData = loadOde('dGeomGetClassData', c_void_p, dGeomID)
dCreateGeom = loadOde('dCreateGeom', dGeomID, c_int32)
dSetColliderOverride = loadOde('dSetColliderOverride', None, c_int32, c_int32, dColliderFn)
