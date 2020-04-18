# -*- coding: utf-8 -*-

from ctypes import POINTER
from ctypes import create_string_buffer
from ctypes import byref
from ctypes import c_char
from ctypes import c_float
from random import random

from odepy import dWorldStep
from odepy import dBodyGetPosition
from odepy import dBodyGetRotation
from odepy import dGeomGetClass
from odepy import dGeomGetBody
from odepy import dGeomSphereGetRadius
from odepy import dSphereClass
from odepy import dCapsuleClass
from odepy import dJointGroupEmpty
from odepy import dSpaceCollide
from odepy import dNearCallback
from odepy import dGeomCapsuleGetParams
from odepy import dReal

from drawstuffpy import DS_VERSION
from drawstuffpy import dsFunctions
from drawstuffpy import dsStartCallback
from drawstuffpy import dsStepCallback
from drawstuffpy import dsSetViewpoint
from drawstuffpy import dsSetColor
from drawstuffpy import dsDrawSphereD
from drawstuffpy import dsDrawCapsuleD
from drawstuffpy import dsSimulationLoop
from drawstuffpy import dsCommandCallback
from drawstuffpy import dsSetSphereQuality

class DrawstuffError(Exception):
    pass

class Drawstuff(object):

    def __init__(self, world, space, contactgroup, geoms, nearCallback,
                 beforeStepCallback=None,
                 commandCallback=None,
                 tDelta=0.01,
                 dsVersion=DS_VERSION,
                 pathToTextures='./ode-0.16.1/drawstuff/textures'.encode('utf-8'),
                 cameraXyz=[3.0, 0.0, 1.0],
                 cameraHpr=[-180.0, 0.0, 0.0],
                 sphereQuality=None):
        self.__world = world
        self.__space = space
        self.__contactgroup = contactgroup
        self.__geoms = geoms
        self.__geomColors = [(random(), random(), random()) for i in self.__geoms]
        self.__nearCallback = nearCallback
        self.__beforeStepCallback = beforeStepCallback
        self.__commandCallback = commandCallback
        self.__tDelta = tDelta
        self.__dsVersion = dsVersion
        self.__pathToTextures = pathToTextures
        self.__cameraXyz = cameraXyz
        self.__cameraHpr = cameraHpr
        self.__sphereQuality = sphereQuality
        self.__fn = dsFunctions()
        self.__SetDrawStuff()

    def __SetDrawStuff(self):
        self.__fn.version = self.__dsVersion
        self.__fn.start = dsStartCallback(self.__StartCallback)
        self.__fn.step = dsStepCallback(self.__StepCallback)
        self.__fn.path_to_textures = create_string_buffer(self.__pathToTextures)
        if self.__commandCallback is not None:
            self.__fn.command = dsCommandCallback(self.__commandCallback)

    def __StartCallback(self):
        xyz = (c_float * 3)()
        hpr = (c_float * 3)()
        for i, v in enumerate(self.__cameraXyz):
            xyz[i] = v
        for i, v in enumerate(self.__cameraHpr):
            hpr[i] = v
        dsSetViewpoint(xyz, hpr)
        if self.__sphereQuality is not None:
            dsSetSphereQuality(self.__sphereQuality)

    def __StepCallback(self, pause):
        if self.__beforeStepCallback is not None:
            self.__beforeStepCallback()
        dSpaceCollide(self.__space, 0, dNearCallback(self.__nearCallback))
        dWorldStep(self.__world, self.__tDelta)
        dJointGroupEmpty(self.__contactgroup)
        for geom, color in zip(self.__geoms, self.__geomColors):
            body = dGeomGetBody(geom)
            if dGeomGetClass(geom) == dSphereClass:
                r = dGeomSphereGetRadius(geom)
                pos = dBodyGetPosition(body)
                rot = dBodyGetRotation(body)
                dsSetColor(*color)
                dsDrawSphereD(pos, rot, r)
            elif dGeomGetClass(geom) == dCapsuleClass:
                r = dReal()
                l = dReal()
                dGeomCapsuleGetParams(geom, byref(r), byref(l))
                pos = dBodyGetPosition(body)
                rot = dBodyGetRotation(body)
                dsSetColor(*color)
                dsDrawCapsuleD(pos, rot, l.value, r.value)
            else:
                raise DrawstuffError('Not supported geom class: {}'.format(dGeomGetClass(geom)))

    def Run(self):
        argc = 0
        argv = byref(POINTER(c_char)())
        w = 800
        h = 450
        dsSimulationLoop(argc, argv, w, h, self.__fn)
