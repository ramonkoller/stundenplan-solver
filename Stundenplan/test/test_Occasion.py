import unittest

from Occasion import Occasion


class TestOccasion(unittest.TestCase):

    def setUp(self):
        self.occasion = Occasion("6aa15d48-c81c-493e-a978-000808bd963e", "7784d658-9551-45b0-b026-09fcf43e763c", "TA.BA_PDP1", "P", 2, 10, True, ["Mo 2","Di 3"], ["_TA"], ["1c41e4ea-77fe-4351-b73a-9e6ca163dc6c"], None)

    def test_occasions_id(self):
        self.assertEquals("6aa15d48-c81c-493e-a978-000808bd963e", self.occasion.occasions_id)

    def test_module_id(self):
        self.assertEquals("7784d658-9551-45b0-b026-09fcf43e763c", self.occasion.module_id)

    def test_occasion_name(self):
        self.assertEquals("TA.BA_PDP1", self.occasion.occasion_name)

    def test_module_type(self):
        self.assertEquals("P", self.occasion.module_type)

    def test_blocks_per_week(self):
        self.assertEquals(2, self.occasion.blocks_per_week)

    def test_num_students(self):
        self.assertEquals(10, self.occasion.num_students)

    def test_fix(self):
        self.assertEquals(True, self.occasion.fix)

    def test_fix_blocks(self):
        self.assertEquals(["Mo 2","Di 3"], self.occasion.fix_blocks)

    def test_classes_id(self):
        self.assertEquals(["_TA"], self.occasion.classes_names)

    def test_lectures_id(self):
        self.assertEquals(["1c41e4ea-77fe-4351-b73a-9e6ca163dc6c"], self.occasion.lecturers_id)

    def test_rooms_id(self):
        self.assertEquals(None, self.occasion.rooms_id)
