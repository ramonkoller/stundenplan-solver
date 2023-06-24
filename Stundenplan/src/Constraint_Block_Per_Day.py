from datetime import datetime

from Constraint import Constraint


class ConstraintBlockPerDay(Constraint):

    def __init__(self, problem, penalty, muss):
        Constraint.__init__(self, problem, penalty, muss)

    def add_constraint_to_model(self):
        if self.muss:
            for o in self.problem.occasions:
                if not o.fix:
                    for d in self.problem.days:
                        self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                                   for b in range(o.blocks_per_week) for s in d.slots for r in
                                                   o.available_rooms) <= 1, "BlockPerDay_{}_{}_{}".format(o.occasions_id, o.occasion_name, d.day_name))
        else:
            self.problem.pbd = {(o, d): self.problem.model.continuous_var(lb=0, ub=1, name="PenaltyBlockPerDay_{}_{}_{}".format(o.occasions_id, o.occasion_name, d.day_name)) for o in self.problem.occasions for d in self.problem.days}
            for o in self.problem.occasions:
                if not o.fix:
                    for d in self.problem.days:
                        self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                                   for b in range(o.blocks_per_week) for s in d.slots for r in
                                                   o.available_rooms) <= 1 + self.problem.pbd[(o, d)], "BlockPerDay_{}_{}_{}".format(o.occasions_id, o.occasion_name, d.day_name))
            self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pbd[(o, d)] for o in self.problem.occasions for d in self.problem.days)
        print("Constraints One Block Per Day are added", datetime.now())

    def validate(self):
        pass




