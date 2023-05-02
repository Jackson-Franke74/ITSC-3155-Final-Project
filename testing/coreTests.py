from core.session import *
from database.db import Database
import unittest

class PointSystemTests(unittest.TestCase):

    def test_add_points(self):
        points = PointSystem()
        test_user = "user1"
        test_points = 10
        points.add_points(test_user, test_points)
        self.assertAlmostEqual(points.get_points(), 10)

    def test_remove_points(self):
        points = PointSystem()
        test_user = "user1"
        test_points = 10
        points.add_points(test_user, test_points)
        points.remove_points(test_user, 5)
        self.assertAlmostEqual(points.get_points(), 5)
