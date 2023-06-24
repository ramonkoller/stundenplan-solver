import unittest

from Class import Class


class TestClass(unittest.TestCase):

    def setUp(self):
        self.classes = Class("8d19cade-208f-431b-a565-94076efe6681", "M1tz")

    def test_class_id(self):
        self.assertEquals("8d19cade-208f-431b-a565-94076efe6681", self.classes.class_id)

    def test_class_name(self):
        self.assertEquals("M1tz", self.classes.class_name)

    def test_add_monday(self):
        self.classes.add_monday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Mon"])

    def test_add_tuesday(self):
        self.classes.add_tuesday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Tue"])

    def test_add_wednesday(self):
        self.classes.add_wednesday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Wed"])

    def test_add_thursday(self):
        self.classes.add_thursday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Thu"])

    def test_add_friday(self):
        self.classes.add_friday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Fri"])

    def test_add_saturday(self):
        self.classes.add_saturday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.classes.timeframes["Sat"])
