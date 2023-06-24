from datetime import datetime

from Constraint import Constraint


class ConstraintClassesCollisions(Constraint):

    def __init__(self, problem, penalty, muss):
        Constraint.__init__(self, problem, penalty, muss)

    def add_constraint_to_model(self):
        if self.muss:
            for c in self.problem.classes:
                for d in self.problem.days:
                    for s in d.slots:
                        self.problem.model.add(self.problem.model.sum(
                            self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions for b in
                            range(o.blocks_per_week) for r in o.available_rooms if c.class_name in o.classes_names and o.module_type in ["K", "M", "P"]) <= 1, "ClassesCollisions_{}_{}_{}".format(c.class_name, d.day_name, s))

        else:
            self.problem.pc = {(c, d, s): self.problem.model.continuous_var(lb=0, ub=1, name="PenaltyClassesCollisions_{}_{}_{}".format(c.class_name, d.day_name, s)) for c in self.problem.classes
                               for d in self.problem.days for s in d.slots}
            for c in self.problem.classes:
                for d in self.problem.days:
                    for s in d.slots:
                        self.problem.model.add(self.problem.model.sum(
                            self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions for b in
                            range(o.blocks_per_week) for r in o.available_rooms if c.class_name in o.classes_names and o.module_type in ["K", "M", "P"])
                                                <= 1 + self.problem.pc[(c, d, s)], "ClassesCollisions_{}_{}_{}".format(c.class_name, d.day_name, s))
            self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pc[(c, d, s)] for c in self.problem.classes
                                            for d in self.problem.days for s in d.slots)
        print("Constraints Classes No Collisions are added", datetime.now())

    def validate(self):
        pass




