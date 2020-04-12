# -*- coding: utf-8 -*-

from .common import loadOde
from .threading import dThreadingImplementationID
from .threading import dThreadingFunctionsInfo

from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_void_p
from ctypes import c_uint32

class dxThreadingThreadPool(Structure):
    pass

dThreadingThreadPoolID = POINTER(dxThreadingThreadPool)

dThreadingAllocateMultiThreadedImplementation = loadOde('dThreadingAllocateMultiThreadedImplementation', dThreadingImplementationID)
dThreadingImplementationGetFunctions = loadOde('dThreadingImplementationGetFunctions', POINTER(dThreadingFunctionsInfo), dThreadingImplementationID)
dThreadingImplementationShutdownProcessing = loadOde('dThreadingImplementationShutdownProcessing', None, dThreadingImplementationID)
dThreadingImplementationCleanupForRestart = loadOde('dThreadingImplementationCleanupForRestart', None, dThreadingImplementationID)
dThreadingFreeImplementation = loadOde('dThreadingFreeImplementation', None, dThreadingImplementationID)

dThreadReadyToServeCallback = CFUNCTYPE(None, c_void_p)

dExternalThreadingServeMultiThreadedImplementation = loadOde('dExternalThreadingServeMultiThreadedImplementation', None, dThreadingImplementationID, dThreadReadyToServeCallback, c_void_p)
dThreadingAllocateThreadPool = loadOde('dThreadingAllocateThreadPool', dThreadingThreadPoolID, c_uint32, c_uint32, c_uint32, c_void_p)
dThreadingThreadPoolServeMultiThreadedImplementation = loadOde('dThreadingThreadPoolServeMultiThreadedImplementation', None, dThreadingThreadPoolID, dThreadingImplementationID)
dThreadingThreadPoolWaitIdleState = loadOde('dThreadingThreadPoolWaitIdleState', None, dThreadingThreadPoolID)
dThreadingFreeThreadPool = loadOde('dThreadingFreeThreadPool', None, dThreadingThreadPoolID)
