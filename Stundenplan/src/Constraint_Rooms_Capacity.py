class ConstraintRoomsCapacity:

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
        self.problem.prc = {(o, b, r): self.problem.model.continuous_var(lb=0, ub=100) for o in self.problem.occasions
                            for b in range(o.blocks_per_week) for r in self.problem.rooms}
        for o in self.problem.occasions:
            if not o.rooms_id:
                for b in range(o.blocks_per_week):
                    for d in self.problem.days:
                        for s in d.slots:
                            for r in self.problem.rooms:
                                self.problem.model.add(self.problem.x[(o, b, d, s, r)] * o.num_students <= r.capacity + self.problem.prc[(o, b, r)])
        self.problem.objective += self.penalty * self.problem.model.sum(self.problem.prc[(o, b, r)] for o in self.problem.occasions
                            for b in range(o.blocks_per_week) for r in self.problem.rooms)

    def validate(self):
        pass




