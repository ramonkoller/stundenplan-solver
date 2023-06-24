import unittest

from Penalty import Penalty


class TestPenalty(unittest.TestCase):

    def setUp(self):
        self.penalty = Penalty("DozentenKollision", 100)

    def test_penalty_name(self):
        self.assertEqual("DozentenKollision", self.penalty.penalty_name)

    def test_penalty_value(self):
        self.assertEqual(100, self.penalty.penalty_value)
