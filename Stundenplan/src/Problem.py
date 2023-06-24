from datetime import datetime

from docplex.mp.model import Model
from Day import Day


class Problem:

    def __init__(self, problem_id, problem_name):
        self._problem_id = problem_id
        self._problem_name = problem_name
        self._occasions = []
        self._rooms = []
        self._lecturers = []
        self._classes = []
        self._classes_by_id = dict()
        self._classes_by_name = dict()
        self._lecturers_by_id = dict()
        self._penalties = []
        self._days = [Day('Mon', 4), Day('Tue', 4), Day('Wed', 4), Day('Thu', 4), Day('Fri', 4), Day('Sat', 2)]
        self._model = Model(id)
        self._class_ids = set()
        self._lecturer_ids = set()
        self._class_names = set()

    @property
    def problem_id(self):
        return self._problem_id

    @property
    def problem_name(self):
        return self._problem_name

    @property
    def occasions(self):
        return self._occasions

    @property
    def rooms(self):
        return self._rooms

    @property
    def lecturers(self):
        return self._lecturers

    @property
    def classes(self):
        return self._classes

    @property
    def penalties(self):
        return self._penalties

    @property
    def days(self):
        return self._days

    @property
    def model(self):
        return self._model

    @property
    def class_ids(self):
        return self._class_ids

    @property
    def lecturer_ids(self):
        return self._lecturer_ids

    @property
    def class_names(self):
        return self._class_names

    @property
    def classes_by_id(self):
        return self._classes_by_id

    @property
    def classes_by_name(self):
        return self._classes_by_name

    @property
    def lecturers_by_id(self):
        return self._lecturers_by_id

    def add_occasion(self, occasion):
        return self.occasions.append(occasion)

    def add_room(self, room):
        return self.rooms.append(room)

    def add_lecture(self, lecture):
        return self.lecturers.append(lecture)

    def add_class(self, classes):
        return self.classes.append(classes)

    def add_penalty(self, penalty):
        return self.penalties.append(penalty)

    def add_solver_variables(self):
        print("Generate variables", datetime.now())
        self.x = {(o, b, d, s, r): self.model.binary_var(name="x_{}_{}_{}_{}_{}_{}".format(o.occasions_id, o.occasion_name, b, d.day_name, s, r.room_id)) for o in self.occasions for b in range(o.blocks_per_week)
             for d in self.days for s in d.slots for r in o.available_rooms}
        self.objective = {self.model.integer_var(name="objective")}
        self.objective = 0
        print("Variables are added", datetime.now())

    def solve_problem(self):
        print("Solver begins", datetime.now())
        self.model.minimize(self.objective)
        self.model.solve(log_output=True)
        print("Solver has ended", datetime.now())


    def __str__(self):
        return "Problem[" + self.problem_id + ", " + self.problem_name + "]"

