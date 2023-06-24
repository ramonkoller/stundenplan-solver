class ScheduledOccasion:

    def __init__(self, occasion_name, block_nr, day, slot, room_nr):
        self._occasion_name = occasion_name
        self._block_nr = block_nr
        self._day = day
        self._slot = slot
        self._room_nr = room_nr

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def block_nr(self):
        return self._block_nr

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    @property
    def room_nr(self):
        return self._room_nr





