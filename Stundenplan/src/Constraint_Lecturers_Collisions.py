from datetime import datetime

from Constraint import Constraint


class ConstraintLecturersCollisions(Constraint):

    def __init__(self, problem, penalty, muss):
        Constraint.__init__(self, problem, penalty, muss)

    def add_constraint_to_model(self):
        if self.muss:
            for l in self.problem.lecturers:
                for d in self.problem.days:
                    for s in d.slots:
                        self.problem.model.add(self.problem.model.sum(
                            self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions for b in
                            range(o.blocks_per_week) for r in o.available_rooms if l.lecturer_id in o.lecturers_id) <= 1, "LecturersCollisions_{}_{}_{}".format(l.lecturer_name, d.day_name, s))
        else:
            self.problem.pl = {(l, d, s): self.problem.model.continuous_var(lb=0, ub=1, name="PenaltyLecturersCollisions_{}_{}_{}".format(l.lecturer_name, d.day_name, s)) for l in self.problem.lecturers
                               for d in self.problem.days for s in d.slots}
            for l in self.problem.lecturers:
                for d in self.problem.days:
                    for s in d.slots:
                        self.problem.model.add(self.problem.model.sum(
                            self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions for b in
                            range(o.blocks_per_week) for r in o.available_rooms if l.lecturer_id in o.lecturers_id)
                                                <= 1 + self.problem.pl[(l, d, s)], "LecturersCollisions_{}_{}_{}".format(l.lecturer_name, d.day_name, s))
            self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pl[(l, d, s)] for l in self.problem.lecturers
                                            for d in self.problem.days for s in d.slots)
        print("Constraints Lecturers No Collisions are added", datetime.now())

    def validate(self):
        pass




