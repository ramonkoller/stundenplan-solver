class Constraint:

    def __init__(self, problem, penalty, muss):
        self._problem = problem
        self._penalty = penalty
        self._muss = muss

    @property
    def problem(self):
        return self._problem

    @property
    def penalty(self):
        return self._penalty

    @property
    def muss(self):
        return self._muss

