import unittest

from flask import current_app

from app import db, User, Task
from app import create_app

class DemoTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_demo(self):
        self.assertTrue(1 == 1) 