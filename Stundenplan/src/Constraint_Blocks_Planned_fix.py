from datetime import datetime

from Constraint import Constraint


class ConstraintBlocksPlannedFix():

    def __init__(self, problem):
        self._problem = problem

    @property
    def problem(self):
        return self._problem

    def add_constraint_to_model(self):
        for o in self.problem.occasions:
            if o.fix:
                for b, slots in enumerate(o.fix_blocks):
                    day, slot = slots.split(' ', 1)
                    day = self.transform(day)
                    slot = int(slot) - 1
                    self.problem.model.add(self.problem.model.sum(self.problem.x[(o, b, d, slot, r)]
                                               for d in self.problem.days for s in d.slots
                                               for r in o.available_rooms if (d.day_name == day and s == slot)) == 1, "BlocksPlannedFix_{}_{}_{}".format(o.occasions_id, o.occasion_name, b))
        print("Constraints Blocks Planned Fix are added", datetime.now())

    def transform(self, german):
        if german == "Mo":
            return "Mon"
        elif german == "Di":
            return "Tue"
        elif german == "Mi":
            return "Wed"
        elif german == "Do":
            return "Thu"
        elif german == "Fr":
            return "Fri"
        elif german == "Sa":
            return "Sat"

    def validate(self):
        pass




