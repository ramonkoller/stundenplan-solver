import unittest

from Day import Day


class TestDay(unittest.TestCase):

    def setUp(self):
        self.day = Day("Monday", 4)

    def test_day_name(self):
        self.assertEqual("Monday", self.day.day_name)

    def test_slots(self):
        self.assertEqual([0, 1, 2, 3], self.day.slots)
