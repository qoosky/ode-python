# -*- coding: utf-8 -*-

from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import c_int32
from ctypes import c_uint32
from ctypes import c_char
from ctypes import c_void_p
from ctypes import c_uint64

class dxThreadingImplementation(Structure):
    pass

dThreadingImplementationID = POINTER(dxThreadingImplementation)

dmutexindex_t = c_uint32

class dxMutexGroup(Structure):
    pass

dMutexGroupID = POINTER(dxMutexGroup)

dMutexGroupAllocFunction = CFUNCTYPE(dMutexGroupID, dThreadingImplementationID, dmutexindex_t, POINTER(POINTER(c_char)))
dMutexGroupFreeFunction = CFUNCTYPE(None, dThreadingImplementationID, dMutexGroupID)
dMutexGroupMutexLockFunction = CFUNCTYPE(None, dThreadingImplementationID, dMutexGroupID, dmutexindex_t)
dMutexGroupMutexUnlockFunction = CFUNCTYPE(None, dThreadingImplementationID, dMutexGroupID, dmutexindex_t)

class dxCallReleasee(Structure):
    pass

dCallReleaseeID = POINTER(dxCallReleasee)

class dxCallWait(Structure):
    pass

dCallWaitID = POINTER(dxCallWait)

ddependencycount_t = c_uint32
ddependencychange_t = c_int32
dcallindex_t = c_uint32

dThreadedCallFunction = CFUNCTYPE(c_int32, c_void_p, dcallindex_t, dCallReleaseeID)

class dThreadedWaitTime(Structure):

    _fields_ = [('wait_sec', c_uint64),
                ('wait_nsec', c_uint64)]

    def _init_(self, wait_sec, wait_nsec):
        self.wait_sec = wait_sec
        self.wait_nsec = wait_nsec

dThreadedCallWaitAllocFunction = CFUNCTYPE(dCallWaitID, dThreadingImplementationID)
dThreadedCallWaitResetFunction = CFUNCTYPE(None, dThreadingImplementationID, dCallWaitID)
dThreadedCallWaitFreeFunction = CFUNCTYPE(None, dThreadingImplementationID, dCallWaitID)
dThreadedCallPostFunction = CFUNCTYPE(None, dThreadingImplementationID, POINTER(c_int32),
                                      POINTER(dCallReleaseeID), ddependencycount_t, dCallReleaseeID,
                                      dCallWaitID, dThreadedCallFunction, c_void_p, dcallindex_t,
                                      POINTER(c_char))
dThreadedCallDependenciesCountAlterFunction = CFUNCTYPE(None, dThreadingImplementationID, dCallReleaseeID, ddependencychange_t)
dThreadedCallWaitFunction = CFUNCTYPE(None, dThreadingImplementationID, POINTER(c_int32),
                                      dCallWaitID, POINTER(dThreadedWaitTime),
                                      POINTER(c_char))
dThreadingImplThreadCountRetrieveFunction = CFUNCTYPE(c_uint32, dThreadingImplementationID)
dThreadingImplResourcesForCallsPreallocateFunction = CFUNCTYPE(c_int32, dThreadingImplementationID, ddependencycount_t)

class dThreadingFunctionsInfo(Structure):

    _fields_ = [('struct_size', c_uint32),
                ('alloc_mutex_group', dMutexGroupAllocFunction),
                ('free_mutex_group', dMutexGroupFreeFunction),
                ('lock_group_mutex', dMutexGroupMutexLockFunction),
                ('unlock_group_mutex', dMutexGroupMutexUnlockFunction),
                ('alloc_call_wait', dThreadedCallWaitAllocFunction),
                ('reset_call_wait', dThreadedCallWaitResetFunction),
                ('free_call_wait', dThreadedCallWaitFreeFunction),
                ('post_call', dThreadedCallPostFunction),
                ('alter_call_dependencies_count', dThreadedCallDependenciesCountAlterFunction),
                ('wait_call', dThreadedCallWaitFunction),
                ('retrieve_thread_count', dThreadingImplThreadCountRetrieveFunction),
                ('preallocate_resources_for_calls', dThreadingImplResourcesForCallsPreallocateFunction)]

    def _init_(self, struct_size, alloc_mutex_group, free_mutex_group, lock_group_mutex, unlock_group_mutex, alloc_call_wait, reset_call_wait, free_call_wait, post_call, alter_call_dependencies_count, wait_call, retrieve_thread_count, preallocate_resources_for_calls):
        self.struct_size = struct_size
        self.alloc_mutex_group = alloc_mutex_group
        self.free_mutex_group = free_mutex_group
        self.lock_group_mutex = lock_group_mutex
        self.unlock_group_mutex = unlock_group_mutex
        self.alloc_call_wait = alloc_call_wait
        self.reset_call_wait = reset_call_wait
        self.free_call_wait = free_call_wait
        self.post_call = post_call
        self.alter_call_dependencies_count = alter_call_dependencies_count
        self.wait_call = wait_call
        self.retrieve_thread_count = retrieve_thread_count
        self.preallocate_resources_for_calls = preallocate_resources_for_calls
