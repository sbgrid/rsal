#!/usr/bin/env python

from flask import Flask
from unittest import TestCase
import requests
import dv

class TestDV(TestCase):
    def setUp(self):
        dv.app.testing=True
        self.app = dv.app.test_client()
    def test_index(self):
        r=self.app.get('/')
        self.assertEqual(200,r.status_code)

