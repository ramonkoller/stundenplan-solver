class Day:

    def __init__(self, day_name, slots):
        self._day_name = day_name
        self._slots = [i for i in range(slots)]

    @property
    def day_name(self):
        return self._day_name

    @property
    def slots(self):
        return self._slots

