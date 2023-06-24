import unittest

from Lecturer import Lecturer


class TestLecture(unittest.TestCase):

    def setUp(self):
        self.lecture = Lecturer("088308cd-b0ed-4099-9be7-0c4ba798a29f", "DiehlR")

    def test_lecture_id(self):
        self.assertEquals("088308cd-b0ed-4099-9be7-0c4ba798a29f", self.lecture.lecturer_id)

    def test_lecture_name(self):
        self.assertEquals("DiehlR", self.lecture.lecturer_name)

    def test_add_monday(self):
        self.lecture.add_monday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Mon"])

    def test_add_tuesday(self):
        self.lecture.add_tuesday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Tue"])

    def test_add_wednesday(self):
        self.lecture.add_wednesday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Wed"])

    def test_add_thursday(self):
        self.lecture.add_thursday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Thu"])

    def test_add_friday(self):
        self.lecture.add_friday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Fri"])

    def test_add_saturday(self):
        self.lecture.add_saturday([0, 1, 3, -3])
        self.assertEquals([0, 1, 3, -3], self.lecture.timeframes["Sat"])
