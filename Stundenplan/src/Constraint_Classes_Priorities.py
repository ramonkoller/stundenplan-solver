from datetime import datetime


class ConstraintClassesPriorities:

    def __init__(self, problem, penalty_list, muss):
        self._problem = problem
        self._penalty_list = penalty_list
        self._muss = muss

    @property
    def problem(self):
        return self._problem

    @property
    def penalty_list(self):
        return self._penalty_list

    @property
    def muss(self):
        return self._muss

    def add_constraint_to_model(self):
        priorities_classes = dict()
        for c in self.problem.classes:
            for d in self.problem.days:
                for s in d.slots:
                    if c.timeframes[d.day_name][s] == 3:
                        priorities_classes[(c, d, s)] = self.penalty_list[0]
                    elif c.timeframes[d.day_name][s] == 2:
                        priorities_classes[(c, d, s)] = self.penalty_list[1]
                    elif c.timeframes[d.day_name][s] == 1:
                        priorities_classes[(c, d, s)] = self.penalty_list[2]
                    elif c.timeframes[d.day_name][s] == 0:
                        priorities_classes[(c, d, s)] = self.penalty_list[3]
                    elif c.timeframes[d.day_name][s] == -1:
                        priorities_classes[(c, d, s)] = self.penalty_list[4]
                    elif c.timeframes[d.day_name][s] == -2:
                        priorities_classes[(c, d, s)] = self.penalty_list[5]
                    elif c.timeframes[d.day_name][s] == -3:
                        priorities_classes[(c, d, s)] = self.penalty_list[6]
        if self.muss:
            for o in self.problem.occasions:
                if not o.fix:
                    for b in range(o.blocks_per_week):
                        for d in self.problem.days:
                            for s in d.slots:
                                for r in o.available_rooms:
                                    for c_name in o.classes_names:
                                        for c in self.problem.classes:
                                            if c_name == c.class_name:
                                                if c.timeframes[d.day_name][s] == -3:
                                                    self.problem.model.add(self.problem.x[(o, b, d, s, r)] <= 0, "ClassesPriorities_{}_{}_{}_{}_{}_{}".format(o.occasions_id, o.occasion_name, b,d.day_name, s, r.room_id))
        self.problem.objective += self.problem.model.sum(self.problem.x[(o, b, d, s, r)] * priorities_classes[(self.problem.classes_by_name[c_name], d, s)] for o in self.problem.occasions for d in self.problem.days for s in d.slots for r in o.available_rooms for b in range(o.blocks_per_week) for c_name in o.classes_names if not o.fix and c_name in self.problem.class_names)
        print("Constraints Classes Priorities are added", datetime.now())

    def validate(self):
        pass




