from datetime import datetime


class ConstraintClassesCompact:

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
        self.problem.chc = {(c, d, s): self.problem.model.binary_var(name="PenaltyClassesCompact1_{}_{}_{}".format(c.class_name, d.day_name, s)) for c in self.problem.classes
                            for d in self.problem.days for s in d.slots}
        self.problem.pcc = {(c, d): self.problem.model.binary_var(name="PenaltyClassesCompact2_{}_{}".format(c.class_name, d.day_name)) for c in self.problem.classes
                            for d in self.problem.days}
        for c in self.problem.classes:
            for d in self.problem.days:
                for s in d.slots:
                    self.problem.model.add(
                        self.problem.model.sum(self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions
                            for b in range(o.blocks_per_week) for r in o.available_rooms if c.class_name in o.classes_names
                            and o.module_type in ["K", "M", "P"]) <= self.problem.chc[(c, d, s)] * 10, "ClassesCompact1_{}_{}_{}".format(c.class_name, d.day_name, s))
                    self.problem.model.add(
                        self.problem.model.sum(self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions
                                               for b in range(o.blocks_per_week) for r in o.available_rooms if
                                               c.class_name in o.classes_names
                                               and o.module_type in ["K", "M", "P"]) >= self.problem.chc[
                            (c, d, s)], "ClassesCompact2_{}_{}_{}".format(c.class_name, d.day_name, s))
        for c in self.problem.classes:
            for d in self.problem.days:
                if d.day_name != "Sat":
                    self.problem.model.add(self.problem.pcc[(c, d)] + self.problem.chc[(c, d, 2)] >= (self.problem.chc[(c, d, 3)] + self.problem.chc[(c, d, 1)] - 1), "ClassesCompact3_{}_{}".format(c.class_name, d.day_name))
                    self.problem.model.add(self.problem.pcc[(c, d)] + self.problem.chc[(c, d, 1)] >= (self.problem.chc[(c, d, 2)] + self.problem.chc[(c, d, 0)] - 1), "ClassesCompact4_{}_{}".format(c.class_name, d.day_name))
                    self.problem.model.add(self.problem.pcc[(c, d)] + self.problem.chc[(c, d, 1)] + self.problem.chc[(c, d, 2)] + 1 >= (self.problem.chc[(c, d, 3)] + self.problem.chc[(c, d, 0)]), "ClassesCompact5{}_{}".format(c.class_name, d.day_name))
        self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pcc[(c, d)] for c in self.problem.classes for d in self.problem.days)
        print("Constraints Classes Compact are added", datetime.now())

    def validate(self):
        pass




