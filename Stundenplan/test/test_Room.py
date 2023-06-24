import unittest

from Room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("f5d666d8-ee31-4be2-8ed4-0017126d54f7", "I.S1A_303", "Innovation Space", 80, False)

    def test_room_id(self):
        self.assertEquals("f5d666d8-ee31-4be2-8ed4-0017126d54f7", self.room.room_id)

    def test_room_nr(self):
        self.assertEquals("I.S1A_303", self.room.room_nr)

    def test_room_name(self):
        self.assertEquals("Innovation Space", self.room.room_name)

    def test_capacity(self):
        self.assertEquals(80, self.room.capacity)

    def test_virtual(self):
        self.assertEquals(False, self.room.virtual)
