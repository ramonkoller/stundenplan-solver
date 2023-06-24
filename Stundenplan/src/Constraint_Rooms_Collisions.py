from datetime import datetime

from Constraint import Constraint


class ConstraintRoomsCollisions(Constraint):

    def __init__(self, problem, penalty, muss):
        Constraint.__init__(self, problem, penalty, muss)

    def add_constraint_to_model(self):
        if self.muss:
            for r in self.problem.rooms:
                if r.virtual:
                    continue
                else:
                    for d in self.problem.days:
                        for s in d.slots:
                            self.problem.model.add(self.problem.model.sum(
                                self.problem.x[(o, b, d, s, r)] for o in r.available_occasions for b in
                                range(o.blocks_per_week)) <= 1, "RoomsCollisions_{}_{}_{}".format(r.room_name, d.day_name, s))

        else:
            self.problem.pr = {(r, d, s): self.problem.model.continuous_var(lb=0, ub=1, name="PenaltyRoomsCollisions_{}_{}_{}".format(r.room_id, d.day_name, s)) for r in self.problem.rooms
                               for d in self.problem.days for s in d.slots if not r.virtual}
            for r in self.problem.rooms:
                if r.virtual:
                    continue
                else:
                    for d in self.problem.days:
                        for s in d.slots:
                            self.problem.model.add(self.problem.model.sum(
                                self.problem.x[(o, b, d, s, r)] for o in r.available_occasions for b in
                                range(o.blocks_per_week)) <= 1 + self.problem.pr[(r, d, s)], "RoomsCollisions_{}_{}_{}".format(r.room_id, d.day_name, s))
            self.problem.objective += self.penalty * self.problem.model.sum(self.problem.pr[(r, d, s)] for r in self.problem.rooms
                                            for d in self.problem.days for s in d.slots if not r.virtual)
        print("Constraints Rooms No Collisions are added", datetime.now())

    def validate(self):
        pass




