import unittest

from Class import Class
from Day import Day
from Lecturer import Lecturer
from Occasion import Occasion
from Penalty import Penalty
from Problem import Problem
from Room import Room


class TestProblem(unittest.TestCase):

    def setUp(self):
        self.problem = Problem("e2ba97fb-5a45-4545-b760-71e19c8e2abe","H21")

    def test_problem_id(self):
        self.assertEqual("e2ba97fb-5a45-4545-b760-71e19c8e2abe", self.problem.problem_id)

    def test_problem_name(self):
        self.assertEqual("H21", self.problem.problem_name)

    def test_occasions(self):
        occasion = Occasion("6aa15d48-c81c-493e-a978-000808bd963e", "7784d658-9551-45b0-b026-09fcf43e763c", "TA.BA_PDP1", "P", 2, 10, True, ["Mo 2","Di 3"], ["_TA"], ["1c41e4ea-77fe-4351-b73a-9e6ca163dc6c"], None)
        self.problem.add_occasion(occasion)
        self.assertEqual([occasion], self.problem.occasions)

    def test_occasions2(self):
        occasion = Occasion("6aa15d48-c81c-493e-a978-000808bd963e", "7784d658-9551-45b0-b026-09fcf43e763c",
                            "TA.BA_PDP1", "P", 2, 10, True, ["Mo 2", "Di 3"], ["_TA"],
                            ["1c41e4ea-77fe-4351-b73a-9e6ca163dc6c"], None)
        self.problem.add_occasion(occasion)
        self.problem.add_occasion(occasion)
        self.assertEqual(2, len(self.problem.occasions))

    def test_rooms(self):
        room = Room("f5d666d8-ee31-4be2-8ed4-0017126d54f7", "I.S1A_303", "Innovation Space", 80, False)
        self.problem.add_room(room)
        self.assertEqual([room], self.problem.rooms)

    def test_lectures(self):
        lecture = Lecturer("088308cd-b0ed-4099-9be7-0c4ba798a29f", "DiehlR")
        self.problem.add_lecture(lecture)
        self.assertEqual([lecture], self.problem.lecturers)

    def test_classes(self):
        classes = Class("8d19cade-208f-431b-a565-94076efe6681", "M1tz")
        self.problem.add_class(classes)
        self.assertEqual([classes], self.problem.classes)

    def test_penalties(self):
        penalty = Penalty("DozentenKollision", 100)
        self.problem.add_penalty(penalty)
        self.assertEqual([penalty], self.problem.penalties)

    def test_days1(self):
        self.assertEqual(6, len(self.problem.days))

    def test_days2(self):
        self.assertEqual([0, 1, 2, 3], self.problem.days[0].slots)

    def test_days3(self):
        self.assertEqual([0, 1], self.problem.days[5].slots)

    def test_days4(self):
        monday = Day('Mon', 4)
        self.problem.add_penalty(monday)
        self.assertEqual(monday.slots, self.problem.days[0].slots)
        self.assertEqual(monday.day_name, self.problem.days[0].day_name)

    def test_days5(self):
        tuesday = Day('Tue', 4)
        self.problem.add_penalty(tuesday)
        self.assertEqual(tuesday.slots, self.problem.days[1].slots)
        self.assertEqual(tuesday.day_name, self.problem.days[1].day_name)

    def test_days6(self):
        wednesday = Day('Wed', 4)
        self.problem.add_penalty(wednesday)
        self.assertEqual(wednesday.slots, self.problem.days[2].slots)
        self.assertEqual(wednesday.day_name, self.problem.days[2].day_name)

    def test_days7(self):
        thursday = Day('Thu', 4)
        self.problem.add_penalty(thursday)
        self.assertEqual(thursday.slots, self.problem.days[3].slots)
        self.assertEqual(thursday.day_name, self.problem.days[3].day_name)

    def test_days8(self):
        friday = Day('Fri', 4)
        self.problem.add_penalty(friday)
        self.assertEqual(friday.slots, self.problem.days[4].slots)
        self.assertEqual(friday.day_name, self.problem.days[4].day_name)

    def test_days9(self):
        saturday = Day('Sat', 2)
        self.problem.add_penalty(saturday)
        self.assertEqual(saturday.slots, self.problem.days[5].slots)
        self.assertEqual(saturday.day_name, self.problem.days[5].day_name)

