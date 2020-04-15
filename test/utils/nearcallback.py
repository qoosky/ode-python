# -*- coding: utf-8 -*-

from ctypes import byref
from ctypes import addressof
from ctypes import sizeof

from odepy import dContact
from odepy import dContactBounce
from odepy import dCollide
from odepy import dJointCreateContact
from odepy import dJointAttach
from odepy import dGeomGetBody

class NearCallbackBounceGround(object):

    def __init__(self, world, contactgroup, groundGeom):
        self.__world = world
        self.__contactgroup = contactgroup
        self.__groundGeom = groundGeom

    def Callback(self, data, o1, o2):
        o1IsGround = addressof(self.__groundGeom.contents) == addressof(o1.contents)
        o2IsGround = addressof(self.__groundGeom.contents) == addressof(o2.contents)
        if not (o1IsGround or o2IsGround):
            return

        N = 10
        contacts = (dContact * N)()
        n = dCollide(o1, o2, N, byref(contacts[0].geom), sizeof(dContact))
        for i in range(n):
            contact = contacts[i]
            contact.surface.mu = float('inf')
            contact.surface.mode = dContactBounce
            contact.surface.bounce = 0.95
            contact.surface.bounce_vel = 0.0
            c = dJointCreateContact(self.__world, self.__contactgroup, byref(contact))
            dJointAttach(c, dGeomGetBody(contact.geom.g1), dGeomGetBody(contact.geom.g2))
