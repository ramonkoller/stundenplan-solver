from datetime import datetime

import regex as re


class ConstraintRoomsPlannedFix:

    def __init__(self, problem):
        self._problem = problem

    @property
    def problem(self):
        return self._problem

    def add_constraint_to_model(self):
        rooms_online = []
        for r in self.problem.rooms:
            match = re.search("Online[0-9]*", r.room_nr)
            if r.virtual or match:
                rooms_online.append(r)
        for o in self.problem.occasions:
            if o.rooms_id:
                for r in o.available_rooms:
                    if o.rooms_id == r.room_id:
                        self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                               for b in range(o.blocks_per_week) for d in self.problem.days for s in d.slots) == o.blocks_per_week, "RoomsPlannedFix_{}_{}_{}".format(r.room_id, o.occasions_id, o.occasion_name))
            else:
                for r in rooms_online:
                    if o in r.available_occasions:
                        self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, s, r)]
                                               for b in range(o.blocks_per_week) for d in self.problem.days for s in
                                               d.slots) == 0, "RoomsPlannedFix_{}_{}_{}".format(r.room_id, o.occasions_id, o.occasion_name))
        print("Constraints Rooms Planned Fix are added", datetime.now())

    def validate(self):
        pass




