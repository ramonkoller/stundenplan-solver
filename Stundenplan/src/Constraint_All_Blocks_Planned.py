from datetime import datetime

from Constraint import Constraint


class ConstraintAllBlocksPlanned(Constraint):

    def __init__(self, problem, penalty, muss):
        Constraint.__init__(self, problem, penalty, muss)

    def add_constraint_to_model(self):
        if self.muss:
            for o in self.problem.occasions:
                for b in range(o.blocks_per_week):
                    self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                               for d in self.problem.days for s in d.slots for r in
                                               o.available_rooms) == 1, "AllBlocksPlanned_{}_{}".format(o.occasions_id, o.occasion_name, b))
        else:
            self.problem.pob = {(o, b): self.problem.model.continuous_var(lb=0, ub=1, name="PenaltyAllBlockPlanned_{}_{}_{}".format(o.occasions_id, o.occasion_name, b)) for o in self.problem.occasions for b in range(o.blocks_per_week)}
            for o in self.problem.occasions:
                for b in range(o.blocks_per_week):
                    self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                                              for d in self.problem.days for s in d.slots for r in
                                                              o.available_rooms) + self.problem.pob[(o, b)] == 1, "AllBlocksPlanned_{}_{}_{}".format(o.occasions_id, o.occasion_name, b))
            self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pob[(o, b)] for o in self.problem.occasions for b in range(o.blocks_per_week))
        print("Constraints All Blocks Planned are added", datetime.now())

    def validate(self):
        pass




