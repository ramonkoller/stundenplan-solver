from datetime import datetime


class ConstraintLecturersCompact:

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
        self.problem.lhc = {(l, d, s): self.problem.model.binary_var(name="PenaltyLecturersCompact1_{}_{}_{}".format(l.lecturer_name, d.day_name, s)) for l in self.problem.lecturers
                            for d in self.problem.days for s in d.slots}
        self.problem.plc = {(l, d): self.problem.model.binary_var(name="PenaltyLecturersCompact2_{}_{}".format(l.lecturer_name, d.day_name)) for l in self.problem.lecturers
                            for d in self.problem.days}
        for l in self.problem.lecturers:
            for d in self.problem.days:
                for s in d.slots:
                    self.problem.model.add(
                        self.problem.model.sum(self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions
                                               for b in range(o.blocks_per_week) for r in o.available_rooms if
                                               l.lecturer_id in o.lecturers_id) <= self.problem.lhc[(l, d, s)] * 10, "LecturersCompact1_{}_{}_{}".format(l.lecturer_name, d.day_name, s))
                    self.problem.model.add(
                        self.problem.model.sum(self.problem.x[(o, b, d, s, r)] for o in self.problem.occasions
                                               for b in range(o.blocks_per_week) for r in o.available_rooms if
                                               l.lecturer_id in o.lecturers_id) >= self.problem.lhc[(l, d, s)], "LecturersCompact2_{}_{}_{}".format(l.lecturer_name, d.day_name, s))
        for l in self.problem.lecturers:
            for d in self.problem.days:
                if d.day_name != "Sat":
                    self.problem.model.add(self.problem.plc[(l, d)] + self.problem.lhc[(l, d, 2)] >= (
                                self.problem.lhc[(l, d, 3)] + self.problem.lhc[(l, d, 1)] - 1), "LecturersCompact3_{}_{}".format(l.lecturer_name, d.day_name))
                    self.problem.model.add(self.problem.plc[(l, d)] + self.problem.lhc[(l, d, 1)] >= (
                                self.problem.lhc[(l, d, 2)] + self.problem.lhc[(l, d, 0)] - 1), "LecturersCompact4_{}_{}".format(l.lecturer_name, d.day_name))
                    self.problem.model.add(
                        self.problem.plc[(l, d)] + self.problem.lhc[(l, d, 1)] + self.problem.lhc[(l, d, 2)] + 1 >= (
                                    self.problem.lhc[(l, d, 3)] + self.problem.lhc[(l, d, 0)]), "LecturersCompact5_{}_{}".format(l.lecturer_name, d.day_name))
        self.problem.objective += self.penalty * self.problem.model.sum(self.problem.plc[(l, d)] for l in self.problem.lecturers for d in self.problem.days)
        print("Constraints Lecturers Compact are added", datetime.now())

    def validate(self):
        pass




