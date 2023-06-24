import unittest

from Scheduled_Occasions import ScheduledOccasion


class TestScheduledOccasion(unittest.TestCase):

    def setUp(self):
        self.scheduled_occasion = ScheduledOccasion("OOP", 2, "Fri", 2, "R302")

    def test_occasion_name(self):
        self.assertEqual("OOP", self.scheduled_occasion.occasion_name)

    def test_block_nr(self):
        self.assertEqual(2, self.scheduled_occasion.block_nr)

    def test_day(self):
        self.assertEqual("Fri", self.scheduled_occasion.day)

    def test_slot(self):
        self.assertEqual(2, self.scheduled_occasion.slot)

    def test_room_name(self):
        self.assertEqual("R302", self.scheduled_occasion.room_name)
