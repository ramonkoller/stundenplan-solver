from datetime import datetime


class ConstraintEveningSaturdaySchool:

    def __init__(self, problem, penalty):
        self._problem = problem
        self._penalty = penalty

    @property
    def problem(self):
        return self._problem

    @property
    def penalty(self):
        return self._penalty

    def add_constraint_to_model(self):
        self.problem.objective += self.penalty * self.problem.model.sum(self.problem.x[(o, b, d, 3, r)] for o in self.problem.occasions for b in range(o.blocks_per_week) for d in self.problem.days for r in o.available_rooms if d.day_name != "Sat")
        self.problem.objective += self.penalty * self.problem.model.sum(
            self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions for b in range(o.blocks_per_week) for d in
            self.problem.days for s in d.slots for r in o.available_rooms if d.day_name == "Sat")
        print("Constraints Evening Or Saturday School are added", datetime.now())

    def validate(self):
        pass




