# -*- coding: utf-8 -*-

from .base import TestBase

from odepy import dNearCallback

class TestSpace(TestBase):

    def test_space(self, space):
        def mycallback(a, b, c):
            pass
        dNearCallback(mycallback)
        assert True
