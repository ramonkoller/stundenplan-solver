from datetime import datetime


class ConstraintLecturersPriorities:

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
        priorities_lecturers = dict()
        for l in self.problem.lecturers:
            for d in self.problem.days:
                for s in d.slots:
                    if l.timeframes[d.day_name][s] == 3:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[0]
                    elif l.timeframes[d.day_name][s] == 2:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[1]
                    elif l.timeframes[d.day_name][s] == 1:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[2]
                    elif l.timeframes[d.day_name][s] == 0:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[3]
                    elif l.timeframes[d.day_name][s] == -1:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[4]
                    elif l.timeframes[d.day_name][s] == -2:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[5]
                    elif l.timeframes[d.day_name][s] == -3:
                        priorities_lecturers[(l, d, s)] = self.penalty_list[6]
        if self.muss:
            for o in self.problem.occasions:
                if not o.fix:
                    for b in range(o.blocks_per_week):
                        for d in self.problem.days:
                            for s in d.slots:
                                for r in o.available_rooms:
                                    for l_id in o.lecturers_id:
                                        for l in self.problem.lecturers:
                                            if l_id == l.lecturer_id:
                                                if l.timeframes[d.day_name][s] == -3:
                                                    self.problem.model.add(self.problem.x[(o, b, d, s, r)] <= 0, "LecturersPriorities_{}_{}_{}_{}_{}_{}".format(o.occasions_id, o.occasion_name, b, d.day_name, s, r.room_id))
        self.problem.objective += self.problem.model.sum(self.problem.x[(o, b, d, s, r)] * priorities_lecturers[(self.problem.lecturers_by_id[l_id], d, s)] for o in self.problem.occasions
                                        for b in range(o.blocks_per_week)
                                        for r in o.available_rooms
                                        for d in self.problem.days for s in d.slots
                                                         for l_id in o.lecturers_id if not o.fix and l_id in self.problem.lecturer_ids)
        print("Constraints Lecturers Priorities are added", datetime.now())

    def validate(self):
        pass




