# -*- coding: utf-8 -*-

from .common import loadOde

from .common import dReal
from .common import dWorldID
from .common import dBodyID
from .common import dVector3
from .common import dMatrix3
from .common import dQuaternion
from .common import dJointID
from .common import dJointType
from .common import dJointGroupID
from .common import dGeomID
from .common import dJointFeedback
from .contact import dContact
from .mass import dMass
from .threading import dThreadingImplementationID
from .threading import dThreadingFunctionsInfo

from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_void_p
from ctypes import c_int32
from ctypes import c_uint32
from ctypes import c_float

dWorldCreate = loadOde('dWorldCreate', dWorldID)
dWorldDestroy = loadOde('dWorldDestroy', None, dWorldID)
dWorldSetData = loadOde('dWorldSetData', None, dWorldID, c_void_p)
dWorldGetData = loadOde('dWorldGetData', c_void_p, dWorldID)
dWorldSetGravity = loadOde('dWorldSetGravity', None, dWorldID, dReal, dReal, dReal)
dWorldGetGravity = loadOde('dWorldGetGravity', None, dWorldID, dVector3)
dWorldSetERP = loadOde('dWorldSetERP', None, dWorldID, dReal)
dWorldGetERP = loadOde('dWorldGetERP', dReal, dWorldID)
dWorldSetCFM = loadOde('dWorldSetCFM', None, dWorldID, dReal)
dWorldGetCFM = loadOde('dWorldGetCFM', dReal, dWorldID)
dWorldSetStepIslandsProcessingMaxThreadCount = loadOde('dWorldSetStepIslandsProcessingMaxThreadCount', None, dWorldID, c_uint32)
dWorldGetStepIslandsProcessingMaxThreadCount = loadOde('dWorldGetStepIslandsProcessingMaxThreadCount', c_uint32, dWorldID)
dWorldUseSharedWorkingMemory = loadOde('dWorldUseSharedWorkingMemory', c_int32, dWorldID, dWorldID)
dWorldCleanupWorkingMemory = loadOde('dWorldCleanupWorkingMemory', None, dWorldID)

class dWorldStepReserveInfo(Structure):

    _fields_ = [('struct_size', c_uint32),
                ('reserve_factor', c_float),
                ('reserve_minimum', c_uint32)]

    def _init_(self, struct_size, reserve_factor, reserve_minimum):
        self.struct_size = struct_size
        self.reserve_factor = reserve_factor
        self.reserve_minimum = reserve_minimum

dWorldSetStepMemoryReservationPolicy = loadOde('dWorldSetStepMemoryReservationPolicy', c_int32, dWorldID, POINTER(dWorldStepReserveInfo))
dWorldSetStepThreadingImplementation = loadOde('dWorldSetStepThreadingImplementation', None, dWorldID, POINTER(dThreadingFunctionsInfo), dThreadingImplementationID)
dWorldStep = loadOde('dWorldStep', c_int32, dWorldID, dReal)
dWorldQuickStep = loadOde('dWorldQuickStep', c_int32, dWorldID, dReal)
dWorldImpulseToForce = loadOde('dWorldImpulseToForce', None, dWorldID, dReal, dReal, dReal, dReal, dVector3)
dWorldSetQuickStepNumIterations = loadOde('dWorldSetQuickStepNumIterations', None, dWorldID, c_int32)
dWorldGetQuickStepNumIterations = loadOde('dWorldGetQuickStepNumIterations', c_int32, dWorldID)
dWorldSetQuickStepW = loadOde('dWorldSetQuickStepW', None, dWorldID, dReal)
dWorldGetQuickStepW = loadOde('dWorldGetQuickStepW', dReal, dWorldID)
dWorldSetContactMaxCorrectingVel = loadOde('dWorldSetContactMaxCorrectingVel', None, dWorldID, dReal)
dWorldGetContactMaxCorrectingVel = loadOde('dWorldGetContactMaxCorrectingVel', dReal, dWorldID)
dWorldSetContactSurfaceLayer = loadOde('dWorldSetContactSurfaceLayer', None, dWorldID, dReal)
dWorldGetContactSurfaceLayer = loadOde('dWorldGetContactSurfaceLayer', dReal, dWorldID)
dWorldGetAutoDisableLinearThreshold = loadOde('dWorldGetAutoDisableLinearThreshold', dReal, dWorldID)
dWorldSetAutoDisableLinearThreshold = loadOde('dWorldSetAutoDisableLinearThreshold', None, dWorldID, dReal)
dWorldGetAutoDisableAngularThreshold = loadOde('dWorldGetAutoDisableAngularThreshold', dReal, dWorldID)
dWorldSetAutoDisableAngularThreshold = loadOde('dWorldSetAutoDisableAngularThreshold', None, dWorldID, dReal)
dWorldGetAutoDisableAverageSamplesCount = loadOde('dWorldGetAutoDisableAverageSamplesCount', c_int32, dWorldID)
dWorldSetAutoDisableAverageSamplesCount = loadOde('dWorldSetAutoDisableAverageSamplesCount', None, dWorldID, c_uint32)
dWorldGetAutoDisableSteps = loadOde('dWorldGetAutoDisableSteps', c_int32, dWorldID)
dWorldSetAutoDisableSteps = loadOde('dWorldSetAutoDisableSteps', None, dWorldID, c_int32)
dWorldGetAutoDisableTime = loadOde('dWorldGetAutoDisableTime', dReal, dWorldID)
dWorldSetAutoDisableTime = loadOde('dWorldSetAutoDisableTime', None, dWorldID, dReal)
dWorldGetAutoDisableFlag = loadOde('dWorldGetAutoDisableFlag', c_int32, dWorldID)
dWorldSetAutoDisableFlag = loadOde('dWorldSetAutoDisableFlag', None, dWorldID, c_int32)
dWorldGetLinearDampingThreshold = loadOde('dWorldGetLinearDampingThreshold', dReal, dWorldID)
dWorldSetLinearDampingThreshold = loadOde('dWorldSetLinearDampingThreshold', None, dWorldID, dReal)
dWorldGetAngularDampingThreshold = loadOde('dWorldGetAngularDampingThreshold', dReal, dWorldID)
dWorldSetAngularDampingThreshold = loadOde('dWorldSetAngularDampingThreshold', None, dWorldID, dReal)
dWorldGetLinearDamping = loadOde('dWorldGetLinearDamping', dReal, dWorldID)
dWorldSetLinearDamping = loadOde('dWorldSetLinearDamping', None, dWorldID, dReal)
dWorldGetAngularDamping = loadOde('dWorldGetAngularDamping', dReal, dWorldID)
dWorldSetAngularDamping = loadOde('dWorldSetAngularDamping', None, dWorldID, dReal)
dWorldSetDamping = loadOde('dWorldSetDamping', None, dWorldID, dReal, dReal)
dWorldGetMaxAngularSpeed = loadOde('dWorldGetMaxAngularSpeed', dReal, dWorldID)
dWorldSetMaxAngularSpeed = loadOde('dWorldSetMaxAngularSpeed', None, dWorldID, dReal)
dBodyGetAutoDisableLinearThreshold = loadOde('dBodyGetAutoDisableLinearThreshold', dReal, dBodyID)
dBodySetAutoDisableLinearThreshold = loadOde('dBodySetAutoDisableLinearThreshold', None, dBodyID, dReal)
dBodyGetAutoDisableAngularThreshold = loadOde('dBodyGetAutoDisableAngularThreshold', dReal, dBodyID)
dBodySetAutoDisableAngularThreshold = loadOde('dBodySetAutoDisableAngularThreshold', None, dBodyID, dReal)
dBodyGetAutoDisableAverageSamplesCount = loadOde('dBodyGetAutoDisableAverageSamplesCount', c_int32, dBodyID)
dBodySetAutoDisableAverageSamplesCount = loadOde('dBodySetAutoDisableAverageSamplesCount', None, dBodyID, c_uint32)
dBodyGetAutoDisableSteps = loadOde('dBodyGetAutoDisableSteps', c_int32, dBodyID)
dBodySetAutoDisableSteps = loadOde('dBodySetAutoDisableSteps', None, dBodyID, c_int32)
dBodyGetAutoDisableTime = loadOde('dBodyGetAutoDisableTime', dReal, dBodyID)
dBodySetAutoDisableTime = loadOde('dBodySetAutoDisableTime', None, dBodyID, dReal)
dBodyGetAutoDisableFlag = loadOde('dBodyGetAutoDisableFlag', c_int32, dBodyID)
dBodySetAutoDisableFlag = loadOde('dBodySetAutoDisableFlag', None, dBodyID, c_int32)
dBodySetAutoDisableDefaults = loadOde('dBodySetAutoDisableDefaults', None, dBodyID)
dBodyGetWorld = loadOde('dBodyGetWorld', dWorldID, dBodyID)
dBodyCreate = loadOde('dBodyCreate', dBodyID, dWorldID)
dBodyDestroy = loadOde('dBodyDestroy', None, dBodyID)
dBodySetData = loadOde('dBodySetData', None, dBodyID, c_void_p)
dBodyGetData = loadOde('dBodyGetData', c_void_p, dBodyID)
dBodySetPosition = loadOde('dBodySetPosition', None, dBodyID, dReal, dReal, dReal)
dBodySetRotation = loadOde('dBodySetRotation', None, dBodyID, dMatrix3)
dBodySetQuaternion = loadOde('dBodySetQuaternion', None, dBodyID, dQuaternion)
dBodySetLinearVel = loadOde('dBodySetLinearVel', None, dBodyID, dReal, dReal, dReal)
dBodySetAngularVel = loadOde('dBodySetAngularVel', None, dBodyID, dReal, dReal, dReal)
dBodyGetPosition = loadOde('dBodyGetPosition', POINTER(dReal), dBodyID)
dBodyCopyPosition = loadOde('dBodyCopyPosition', None, dBodyID, dVector3)
dBodyGetRotation = loadOde('dBodyGetRotation', POINTER(dReal), dBodyID)
dBodyCopyRotation = loadOde('dBodyCopyRotation', None, dBodyID, dMatrix3)
dBodyGetQuaternion = loadOde('dBodyGetQuaternion', POINTER(dReal), dBodyID)
dBodyCopyQuaternion = loadOde('dBodyCopyQuaternion', None, dBodyID, dQuaternion)
dBodyGetLinearVel = loadOde('dBodyGetLinearVel', POINTER(dReal), dBodyID)
dBodyGetAngularVel = loadOde('dBodyGetAngularVel', POINTER(dReal), dBodyID)
dBodySetMass = loadOde('dBodySetMass', None, dBodyID, POINTER(dMass))
dBodyGetMass = loadOde('dBodyGetMass', None, dBodyID, POINTER(dMass))
dBodyAddForce = loadOde('dBodyAddForce', None, dBodyID, dReal, dReal, dReal)
dBodyAddTorque = loadOde('dBodyAddTorque', None, dBodyID, dReal, dReal, dReal)
dBodyAddRelForce = loadOde('dBodyAddRelForce', None, dBodyID, dReal, dReal, dReal)
dBodyAddRelTorque = loadOde('dBodyAddRelTorque', None, dBodyID, dReal, dReal, dReal)
dBodyAddForceAtPos = loadOde('dBodyAddForceAtPos', None, dBodyID, dReal, dReal, dReal, dReal, dReal, dReal)
dBodyAddForceAtRelPos = loadOde('dBodyAddForceAtRelPos', None, dBodyID, dReal, dReal, dReal, dReal, dReal, dReal)
dBodyAddRelForceAtPos = loadOde('dBodyAddRelForceAtPos', None, dBodyID, dReal, dReal, dReal, dReal, dReal, dReal)
dBodyAddRelForceAtRelPos = loadOde('dBodyAddRelForceAtRelPos', None, dBodyID, dReal, dReal, dReal, dReal, dReal, dReal)
dBodyGetForce = loadOde('dBodyGetForce', POINTER(dReal), dBodyID)
dBodyGetTorque = loadOde('dBodyGetTorque', POINTER(dReal), dBodyID)
dBodySetForce = loadOde('dBodySetForce', None, dBodyID, dReal, dReal, dReal)
dBodySetTorque = loadOde('dBodySetTorque', None, dBodyID, dReal, dReal, dReal)
dBodyGetRelPointPos = loadOde('dBodyGetRelPointPos', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodyGetRelPointVel = loadOde('dBodyGetRelPointVel', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodyGetPointVel = loadOde('dBodyGetPointVel', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodyGetPosRelPoint = loadOde('dBodyGetPosRelPoint', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodyVectorToWorld = loadOde('dBodyVectorToWorld', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodyVectorFromWorld = loadOde('dBodyVectorFromWorld', None, dBodyID, dReal, dReal, dReal, dVector3)
dBodySetFiniteRotationMode = loadOde('dBodySetFiniteRotationMode', None, dBodyID, c_int32)
dBodySetFiniteRotationAxis = loadOde('dBodySetFiniteRotationAxis', None, dBodyID, dReal, dReal, dReal)
dBodyGetFiniteRotationMode = loadOde('dBodyGetFiniteRotationMode', c_int32, dBodyID)
dBodyGetFiniteRotationAxis = loadOde('dBodyGetFiniteRotationAxis', None, dBodyID, dVector3)
dBodyGetNumJoints = loadOde('dBodyGetNumJoints', c_int32, dBodyID)
dBodyGetJoint = loadOde('dBodyGetJoint', dJointID, dBodyID, c_int32)
dBodySetDynamic = loadOde('dBodySetDynamic', None, dBodyID)
dBodySetKinematic = loadOde('dBodySetKinematic', None, dBodyID)
dBodyIsKinematic = loadOde('dBodyIsKinematic', c_int32, dBodyID)
dBodyEnable = loadOde('dBodyEnable', None, dBodyID)
dBodyDisable = loadOde('dBodyDisable', None, dBodyID)
dBodyIsEnabled = loadOde('dBodyIsEnabled', c_int32, dBodyID)
dBodySetGravityMode = loadOde('dBodySetGravityMode', None, dBodyID, c_int32)
dBodyGetGravityMode = loadOde('dBodyGetGravityMode', c_int32, dBodyID)
dBodySetMovedCallback = loadOde('dBodySetMovedCallback', None, dBodyID, CFUNCTYPE(None, dBodyID))
dBodyGetFirstGeom = loadOde('dBodyGetFirstGeom', dGeomID, dBodyID)
dBodyGetNextGeom = loadOde('dBodyGetNextGeom', dGeomID, dGeomID)
dBodySetDampingDefaults = loadOde('dBodySetDampingDefaults', None, dBodyID)
dBodyGetLinearDamping = loadOde('dBodyGetLinearDamping', dReal, dBodyID)
dBodySetLinearDamping = loadOde('dBodySetLinearDamping', None, dBodyID, dReal)
dBodyGetAngularDamping = loadOde('dBodyGetAngularDamping', dReal, dBodyID)
dBodySetAngularDamping = loadOde('dBodySetAngularDamping', None, dBodyID, dReal)
dBodySetDamping = loadOde('dBodySetDamping', None, dBodyID, dReal, dReal)
dBodyGetLinearDampingThreshold = loadOde('dBodyGetLinearDampingThreshold', dReal, dBodyID)
dBodySetLinearDampingThreshold = loadOde('dBodySetLinearDampingThreshold', None, dBodyID, dReal)
dBodyGetAngularDampingThreshold = loadOde('dBodyGetAngularDampingThreshold', dReal, dBodyID)
dBodySetAngularDampingThreshold = loadOde('dBodySetAngularDampingThreshold', None, dBodyID, dReal)
dBodyGetMaxAngularSpeed = loadOde('dBodyGetMaxAngularSpeed', dReal, dBodyID)
dBodySetMaxAngularSpeed = loadOde('dBodySetMaxAngularSpeed', None, dBodyID, dReal)
dBodyGetGyroscopicMode = loadOde('dBodyGetGyroscopicMode', c_int32, dBodyID)
dBodySetGyroscopicMode = loadOde('dBodySetGyroscopicMode', None, dBodyID, c_int32)
dJointCreateBall = loadOde('dJointCreateBall', dJointID, dWorldID, dJointGroupID)
dJointCreateHinge = loadOde('dJointCreateHinge', dJointID, dWorldID, dJointGroupID)
dJointCreateSlider = loadOde('dJointCreateSlider', dJointID, dWorldID, dJointGroupID)
dJointCreateContact = loadOde('dJointCreateContact', dJointID, dWorldID, dJointGroupID, POINTER(dContact))
dJointCreateHinge2 = loadOde('dJointCreateHinge2', dJointID, dWorldID, dJointGroupID)
dJointCreateUniversal = loadOde('dJointCreateUniversal', dJointID, dWorldID, dJointGroupID)
dJointCreatePR = loadOde('dJointCreatePR', dJointID, dWorldID, dJointGroupID)
dJointCreatePU = loadOde('dJointCreatePU', dJointID, dWorldID, dJointGroupID)
dJointCreatePiston = loadOde('dJointCreatePiston', dJointID, dWorldID, dJointGroupID)
dJointCreateFixed = loadOde('dJointCreateFixed', dJointID, dWorldID, dJointGroupID)
dJointCreateNull = loadOde('dJointCreateNull', dJointID, dWorldID, dJointGroupID)
dJointCreateAMotor = loadOde('dJointCreateAMotor', dJointID, dWorldID, dJointGroupID)
dJointCreateLMotor = loadOde('dJointCreateLMotor', dJointID, dWorldID, dJointGroupID)
dJointCreatePlane2D = loadOde('dJointCreatePlane2D', dJointID, dWorldID, dJointGroupID)
dJointCreateDBall = loadOde('dJointCreateDBall', dJointID, dWorldID, dJointGroupID)
dJointCreateDHinge = loadOde('dJointCreateDHinge', dJointID, dWorldID, dJointGroupID)
dJointCreateTransmission = loadOde('dJointCreateTransmission', dJointID, dWorldID, dJointGroupID)
dJointDestroy = loadOde('dJointDestroy', None, dJointID)
dJointGroupCreate = loadOde('dJointGroupCreate', dJointGroupID, c_int32)
dJointGroupDestroy = loadOde('dJointGroupDestroy', None, dJointGroupID)
dJointGroupEmpty = loadOde('dJointGroupEmpty', None, dJointGroupID)
dJointGetNumBodies = loadOde('dJointGetNumBodies', c_int32, dJointID)
dJointAttach = loadOde('dJointAttach', None, dJointID, dBodyID, dBodyID)
dJointEnable = loadOde('dJointEnable', None, dJointID)
dJointDisable = loadOde('dJointDisable', None, dJointID)
dJointIsEnabled = loadOde('dJointIsEnabled', c_int32, dJointID)
dJointSetData = loadOde('dJointSetData', None, dJointID, c_void_p)
dJointGetData = loadOde('dJointGetData', c_void_p, dJointID)
dJointGetType = loadOde('dJointGetType', dJointType, dJointID)
dJointGetBody = loadOde('dJointGetBody', dBodyID, dJointID, c_int32)
dJointSetFeedback = loadOde('dJointSetFeedback', None, dJointID, POINTER(dJointFeedback))
dJointGetFeedback = loadOde('dJointGetFeedback', POINTER(dJointFeedback), dJointID)
dJointSetBallAnchor = loadOde('dJointSetBallAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetBallAnchor2 = loadOde('dJointSetBallAnchor2', None, dJointID, dReal, dReal, dReal)
dJointSetBallParam = loadOde('dJointSetBallParam', None, dJointID, c_int32, dReal)
dJointSetHingeAnchor = loadOde('dJointSetHingeAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetHingeAnchorDelta = loadOde('dJointSetHingeAnchorDelta', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetHingeAxis = loadOde('dJointSetHingeAxis', None, dJointID, dReal, dReal, dReal)
dJointSetHingeAxisOffset = loadOde('dJointSetHingeAxisOffset', None, dJointID, dReal, dReal, dReal, dReal)
dJointSetHingeParam = loadOde('dJointSetHingeParam', None, dJointID, c_int32, dReal)
dJointAddHingeTorque = loadOde('dJointAddHingeTorque', None, dJointID, dReal)
dJointSetSliderAxis = loadOde('dJointSetSliderAxis', None, dJointID, dReal, dReal, dReal)
dJointSetSliderAxisDelta = loadOde('dJointSetSliderAxisDelta', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetSliderParam = loadOde('dJointSetSliderParam', None, dJointID, c_int32, dReal)
dJointAddSliderForce = loadOde('dJointAddSliderForce', None, dJointID, dReal)
dJointSetHinge2Anchor = loadOde('dJointSetHinge2Anchor', None, dJointID, dReal, dReal, dReal)
dJointSetHinge2Axes = loadOde('dJointSetHinge2Axes', None, dJointID, POINTER(dReal), POINTER(dReal))
dJointSetHinge2Axis1 = loadOde('dJointSetHinge2Axis1', None, dJointID, dReal, dReal, dReal)
dJointSetHinge2Axis2 = loadOde('dJointSetHinge2Axis2', None, dJointID, dReal, dReal, dReal)
dJointSetHinge2Param = loadOde('dJointSetHinge2Param', None, dJointID, c_int32, dReal)
dJointAddHinge2Torques = loadOde('dJointAddHinge2Torques', None, dJointID, dReal, dReal)
dJointSetUniversalAnchor = loadOde('dJointSetUniversalAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetUniversalAxis1 = loadOde('dJointSetUniversalAxis1', None, dJointID, dReal, dReal, dReal)
dJointSetUniversalAxis1Offset = loadOde('dJointSetUniversalAxis1Offset', None, dJointID, dReal, dReal, dReal, dReal, dReal)
dJointSetUniversalAxis2 = loadOde('dJointSetUniversalAxis2', None, dJointID, dReal, dReal, dReal)
dJointSetUniversalAxis2Offset = loadOde('dJointSetUniversalAxis2Offset', None, dJointID, dReal, dReal, dReal, dReal, dReal)
dJointSetUniversalParam = loadOde('dJointSetUniversalParam', None, dJointID, c_int32, dReal)
dJointAddUniversalTorques = loadOde('dJointAddUniversalTorques', None, dJointID, dReal, dReal)
dJointSetPRAnchor = loadOde('dJointSetPRAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetPRAxis1 = loadOde('dJointSetPRAxis1', None, dJointID, dReal, dReal, dReal)
dJointSetPRAxis2 = loadOde('dJointSetPRAxis2', None, dJointID, dReal, dReal, dReal)
dJointSetPRParam = loadOde('dJointSetPRParam', None, dJointID, c_int32, dReal)
dJointAddPRTorque = loadOde('dJointAddPRTorque', None, dJointID, dReal)
dJointSetPUAnchor = loadOde('dJointSetPUAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetPUAnchorDelta = loadOde('dJointSetPUAnchorDelta', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetPUAnchorOffset = loadOde('dJointSetPUAnchorOffset', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetPUAxis1 = loadOde('dJointSetPUAxis1', None, dJointID, dReal, dReal, dReal)
dJointSetPUAxis2 = loadOde('dJointSetPUAxis2', None, dJointID, dReal, dReal, dReal)
dJointSetPUAxis3 = loadOde('dJointSetPUAxis3', None, dJointID, dReal, dReal, dReal)
dJointSetPUAxisP = loadOde('dJointSetPUAxisP', None, dJointID, dReal, dReal, dReal)
dJointSetPUParam = loadOde('dJointSetPUParam', None, dJointID, c_int32, dReal)
dJointSetPistonAnchor = loadOde('dJointSetPistonAnchor', None, dJointID, dReal, dReal, dReal)
dJointSetPistonAnchorOffset = loadOde('dJointSetPistonAnchorOffset', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetPistonAxis = loadOde('dJointSetPistonAxis', None, dJointID, dReal, dReal, dReal)
dJointSetPistonAxisDelta = loadOde('dJointSetPistonAxisDelta', None, dJointID, dReal, dReal, dReal, dReal, dReal, dReal)
dJointSetPistonParam = loadOde('dJointSetPistonParam', None, dJointID, c_int32, dReal)
dJointAddPistonForce = loadOde('dJointAddPistonForce', None, dJointID, dReal)
dJointSetFixed = loadOde('dJointSetFixed', None, dJointID)
dJointSetFixedParam = loadOde('dJointSetFixedParam', None, dJointID, c_int32, dReal)
dJointSetAMotorNumAxes = loadOde('dJointSetAMotorNumAxes', None, dJointID, c_int32)
dJointSetAMotorAxis = loadOde('dJointSetAMotorAxis', None, dJointID, c_int32, c_int32, dReal, dReal, dReal)
dJointSetAMotorAngle = loadOde('dJointSetAMotorAngle', None, dJointID, c_int32, dReal)
dJointSetAMotorParam = loadOde('dJointSetAMotorParam', None, dJointID, c_int32, dReal)
dJointSetAMotorMode = loadOde('dJointSetAMotorMode', None, dJointID, c_int32)
dJointAddAMotorTorques = loadOde('dJointAddAMotorTorques', None, dJointID, dReal, dReal, dReal)
dJointSetLMotorNumAxes = loadOde('dJointSetLMotorNumAxes', None, dJointID, c_int32)
dJointSetLMotorAxis = loadOde('dJointSetLMotorAxis', None, dJointID, c_int32, c_int32, dReal, dReal, dReal)
dJointSetLMotorParam = loadOde('dJointSetLMotorParam', None, dJointID, c_int32, dReal)
dJointSetPlane2DXParam = loadOde('dJointSetPlane2DXParam', None, dJointID, c_int32, dReal)
dJointSetPlane2DYParam = loadOde('dJointSetPlane2DYParam', None, dJointID, c_int32, dReal)
dJointSetPlane2DAngleParam = loadOde('dJointSetPlane2DAngleParam', None, dJointID, c_int32, dReal)
dJointGetBallAnchor = loadOde('dJointGetBallAnchor', None, dJointID, dVector3)
dJointGetBallAnchor2 = loadOde('dJointGetBallAnchor2', None, dJointID, dVector3)
dJointGetBallParam = loadOde('dJointGetBallParam', dReal, dJointID, c_int32)
dJointGetHingeAnchor = loadOde('dJointGetHingeAnchor', None, dJointID, dVector3)
dJointGetHingeAnchor2 = loadOde('dJointGetHingeAnchor2', None, dJointID, dVector3)
dJointGetHingeAxis = loadOde('dJointGetHingeAxis', None, dJointID, dVector3)
dJointGetHingeParam = loadOde('dJointGetHingeParam', dReal, dJointID, c_int32)
dJointGetHingeAngle = loadOde('dJointGetHingeAngle', dReal, dJointID)
dJointGetHingeAngleRate = loadOde('dJointGetHingeAngleRate', dReal, dJointID)
dJointGetSliderPosition = loadOde('dJointGetSliderPosition', dReal, dJointID)
dJointGetSliderPositionRate = loadOde('dJointGetSliderPositionRate', dReal, dJointID)
dJointGetSliderAxis = loadOde('dJointGetSliderAxis', None, dJointID, dVector3)
dJointGetSliderParam = loadOde('dJointGetSliderParam', dReal, dJointID, c_int32)
dJointGetHinge2Anchor = loadOde('dJointGetHinge2Anchor', None, dJointID, dVector3)
dJointGetHinge2Anchor2 = loadOde('dJointGetHinge2Anchor2', None, dJointID, dVector3)
dJointGetHinge2Axis1 = loadOde('dJointGetHinge2Axis1', None, dJointID, dVector3)
dJointGetHinge2Axis2 = loadOde('dJointGetHinge2Axis2', None, dJointID, dVector3)
dJointGetHinge2Param = loadOde('dJointGetHinge2Param', dReal, dJointID, c_int32)
dJointGetHinge2Angle1 = loadOde('dJointGetHinge2Angle1', dReal, dJointID)
dJointGetHinge2Angle2 = loadOde('dJointGetHinge2Angle2', dReal, dJointID)
dJointGetHinge2Angle1Rate = loadOde('dJointGetHinge2Angle1Rate', dReal, dJointID)
dJointGetHinge2Angle2Rate = loadOde('dJointGetHinge2Angle2Rate', dReal, dJointID)
dJointGetUniversalAnchor = loadOde('dJointGetUniversalAnchor', None, dJointID, dVector3)
dJointGetUniversalAnchor2 = loadOde('dJointGetUniversalAnchor2', None, dJointID, dVector3)
dJointGetUniversalAxis1 = loadOde('dJointGetUniversalAxis1', None, dJointID, dVector3)
dJointGetUniversalAxis2 = loadOde('dJointGetUniversalAxis2', None, dJointID, dVector3)
dJointGetUniversalParam = loadOde('dJointGetUniversalParam', dReal, dJointID, c_int32)
dJointGetUniversalAngles = loadOde('dJointGetUniversalAngles', None, dJointID, POINTER(dReal), POINTER(dReal))
dJointGetUniversalAngle1 = loadOde('dJointGetUniversalAngle1', dReal, dJointID)
dJointGetUniversalAngle2 = loadOde('dJointGetUniversalAngle2', dReal, dJointID)
dJointGetUniversalAngle1Rate = loadOde('dJointGetUniversalAngle1Rate', dReal, dJointID)
dJointGetUniversalAngle2Rate = loadOde('dJointGetUniversalAngle2Rate', dReal, dJointID)
dJointGetPRAnchor = loadOde('dJointGetPRAnchor', None, dJointID, dVector3)
dJointGetPRPosition = loadOde('dJointGetPRPosition', dReal, dJointID)
dJointGetPRPositionRate = loadOde('dJointGetPRPositionRate', dReal, dJointID)
dJointGetPRAngle = loadOde('dJointGetPRAngle', dReal, dJointID)
dJointGetPRAngleRate = loadOde('dJointGetPRAngleRate', dReal, dJointID)
dJointGetPRAxis1 = loadOde('dJointGetPRAxis1', None, dJointID, dVector3)
dJointGetPRAxis2 = loadOde('dJointGetPRAxis2', None, dJointID, dVector3)
dJointGetPRParam = loadOde('dJointGetPRParam', dReal, dJointID, c_int32)
dJointGetPUAnchor = loadOde('dJointGetPUAnchor', None, dJointID, dVector3)
dJointGetPUPosition = loadOde('dJointGetPUPosition', dReal, dJointID)
dJointGetPUPositionRate = loadOde('dJointGetPUPositionRate', dReal, dJointID)
dJointGetPUAxis1 = loadOde('dJointGetPUAxis1', None, dJointID, dVector3)
dJointGetPUAxis2 = loadOde('dJointGetPUAxis2', None, dJointID, dVector3)
dJointGetPUAxis3 = loadOde('dJointGetPUAxis3', None, dJointID, dVector3)
dJointGetPUAxisP = loadOde('dJointGetPUAxisP', None, dJointID, dVector3)
dJointGetPUAngles = loadOde('dJointGetPUAngles', None, dJointID, POINTER(dReal), POINTER(dReal))
dJointGetPUAngle1 = loadOde('dJointGetPUAngle1', dReal, dJointID)
dJointGetPUAngle1Rate = loadOde('dJointGetPUAngle1Rate', dReal, dJointID)
dJointGetPUAngle2 = loadOde('dJointGetPUAngle2', dReal, dJointID)
dJointGetPUAngle2Rate = loadOde('dJointGetPUAngle2Rate', dReal, dJointID)
dJointGetPUParam = loadOde('dJointGetPUParam', dReal, dJointID, c_int32)
dJointGetPistonPosition = loadOde('dJointGetPistonPosition', dReal, dJointID)
dJointGetPistonPositionRate = loadOde('dJointGetPistonPositionRate', dReal, dJointID)
dJointGetPistonAngle = loadOde('dJointGetPistonAngle', dReal, dJointID)
dJointGetPistonAngleRate = loadOde('dJointGetPistonAngleRate', dReal, dJointID)
dJointGetPistonAnchor = loadOde('dJointGetPistonAnchor', None, dJointID, dVector3)
dJointGetPistonAnchor2 = loadOde('dJointGetPistonAnchor2', None, dJointID, dVector3)
dJointGetPistonAxis = loadOde('dJointGetPistonAxis', None, dJointID, dVector3)
dJointGetPistonParam = loadOde('dJointGetPistonParam', dReal, dJointID, c_int32)
dJointGetAMotorNumAxes = loadOde('dJointGetAMotorNumAxes', c_int32, dJointID)
dJointGetAMotorAxis = loadOde('dJointGetAMotorAxis', None, dJointID, c_int32, dVector3)
dJointGetAMotorAxisRel = loadOde('dJointGetAMotorAxisRel', c_int32, dJointID, c_int32)
dJointGetAMotorAngle = loadOde('dJointGetAMotorAngle', dReal, dJointID, c_int32)
dJointGetAMotorAngleRate = loadOde('dJointGetAMotorAngleRate', dReal, dJointID, c_int32)
dJointGetAMotorParam = loadOde('dJointGetAMotorParam', dReal, dJointID, c_int32)
dJointGetAMotorMode = loadOde('dJointGetAMotorMode', c_int32, dJointID)
dJointGetLMotorNumAxes = loadOde('dJointGetLMotorNumAxes', c_int32, dJointID)
dJointGetLMotorAxis = loadOde('dJointGetLMotorAxis', None, dJointID, c_int32, dVector3)
dJointGetLMotorParam = loadOde('dJointGetLMotorParam', dReal, dJointID, c_int32)
dJointGetFixedParam = loadOde('dJointGetFixedParam', dReal, dJointID, c_int32)
dJointGetTransmissionContactPoint1 = loadOde('dJointGetTransmissionContactPoint1', None, dJointID, dVector3)
dJointGetTransmissionContactPoint2 = loadOde('dJointGetTransmissionContactPoint2', None, dJointID, dVector3)
dJointSetTransmissionAxis1 = loadOde('dJointSetTransmissionAxis1', None, dJointID, dReal, dReal, dReal)
dJointGetTransmissionAxis1 = loadOde('dJointGetTransmissionAxis1', None, dJointID, dVector3)
dJointSetTransmissionAxis2 = loadOde('dJointSetTransmissionAxis2', None, dJointID, dReal, dReal, dReal)
dJointGetTransmissionAxis2 = loadOde('dJointGetTransmissionAxis2', None, dJointID, dVector3)
dJointSetTransmissionAnchor1 = loadOde('dJointSetTransmissionAnchor1', None, dJointID, dReal, dReal, dReal)
dJointGetTransmissionAnchor1 = loadOde('dJointGetTransmissionAnchor1', None, dJointID, dVector3)
dJointSetTransmissionAnchor2 = loadOde('dJointSetTransmissionAnchor2', None, dJointID, dReal, dReal, dReal)
dJointGetTransmissionAnchor2 = loadOde('dJointGetTransmissionAnchor2', None, dJointID, dVector3)
dJointSetTransmissionParam = loadOde('dJointSetTransmissionParam', None, dJointID, c_int32, dReal)
dJointGetTransmissionParam = loadOde('dJointGetTransmissionParam', dReal, dJointID, c_int32)
dJointSetTransmissionMode = loadOde('dJointSetTransmissionMode', None, dJointID, c_int32)
dJointGetTransmissionMode = loadOde('dJointGetTransmissionMode', c_int32, dJointID)
dJointSetTransmissionRatio = loadOde('dJointSetTransmissionRatio', None, dJointID, dReal)
dJointGetTransmissionRatio = loadOde('dJointGetTransmissionRatio', dReal, dJointID)
dJointSetTransmissionAxis = loadOde('dJointSetTransmissionAxis', None, dJointID, dReal, dReal, dReal)
dJointGetTransmissionAxis = loadOde('dJointGetTransmissionAxis', None, dJointID, dVector3)
dJointGetTransmissionAngle1 = loadOde('dJointGetTransmissionAngle1', dReal, dJointID)
dJointGetTransmissionAngle2 = loadOde('dJointGetTransmissionAngle2', dReal, dJointID)
dJointGetTransmissionRadius1 = loadOde('dJointGetTransmissionRadius1', dReal, dJointID)
dJointGetTransmissionRadius2 = loadOde('dJointGetTransmissionRadius2', dReal, dJointID)
dJointSetTransmissionRadius1 = loadOde('dJointSetTransmissionRadius1', None, dJointID, dReal)
dJointSetTransmissionRadius2 = loadOde('dJointSetTransmissionRadius2', None, dJointID, dReal)
dJointGetTransmissionBacklash = loadOde('dJointGetTransmissionBacklash', dReal, dJointID)
dJointSetTransmissionBacklash = loadOde('dJointSetTransmissionBacklash', None, dJointID, dReal)
dJointSetDBallAnchor1 = loadOde('dJointSetDBallAnchor1', None, dJointID, dReal, dReal, dReal)
dJointSetDBallAnchor2 = loadOde('dJointSetDBallAnchor2', None, dJointID, dReal, dReal, dReal)
dJointGetDBallAnchor1 = loadOde('dJointGetDBallAnchor1', None, dJointID, dVector3)
dJointGetDBallAnchor2 = loadOde('dJointGetDBallAnchor2', None, dJointID, dVector3)
dJointGetDBallDistance = loadOde('dJointGetDBallDistance', dReal, dJointID)
dJointSetDBallDistance = loadOde('dJointSetDBallDistance', None, dJointID, dReal)
dJointSetDBallParam = loadOde('dJointSetDBallParam', None, dJointID, c_int32, dReal)
dJointGetDBallParam = loadOde('dJointGetDBallParam', dReal, dJointID, c_int32)
dJointSetDHingeAxis = loadOde('dJointSetDHingeAxis', None, dJointID, dReal, dReal, dReal)
dJointGetDHingeAxis = loadOde('dJointGetDHingeAxis', None, dJointID, dVector3)
dJointSetDHingeAnchor1 = loadOde('dJointSetDHingeAnchor1', None, dJointID, dReal, dReal, dReal)
dJointSetDHingeAnchor2 = loadOde('dJointSetDHingeAnchor2', None, dJointID, dReal, dReal, dReal)
dJointGetDHingeAnchor1 = loadOde('dJointGetDHingeAnchor1', None, dJointID, dVector3)
dJointGetDHingeAnchor2 = loadOde('dJointGetDHingeAnchor2', None, dJointID, dVector3)
dJointGetDHingeDistance = loadOde('dJointGetDHingeDistance', dReal, dJointID)
dJointSetDHingeParam = loadOde('dJointSetDHingeParam', None, dJointID, c_int32, dReal)
dJointGetDHingeParam = loadOde('dJointGetDHingeParam', dReal, dJointID, c_int32)
dConnectingJoint = loadOde('dConnectingJoint', dJointID, dBodyID, dBodyID)
dConnectingJointList = loadOde('dConnectingJointList', c_int32, dBodyID, dBodyID, POINTER(dJointID))
dAreConnected = loadOde('dAreConnected', c_int32, dBodyID, dBodyID)
dAreConnectedExcluding = loadOde('dAreConnectedExcluding', c_int32, dBodyID, dBodyID, c_int32)
