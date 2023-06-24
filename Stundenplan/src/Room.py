class Room:

    def __init__(self, room_id, room_nr, room_name, capacitiy, virtual):
        self._room_id = room_id
        self._room_nr = room_nr
        self._room_name = room_name
        self._capacity = capacitiy
        self._virtual = virtual
        self._available_occasions = []

    @property
    def room_id(self):
        return self._room_id

    @property
    def room_nr(self):
        return self._room_nr

    @property
    def room_name(self):
        return self._room_name

    @property
    def capacity(self):
        return self._capacity

    @property
    def virtual(self):
        return self._virtual

    @property
    def available_occasions(self):
        return self._available_occasions

    def add_available_occasion(self, available_occasion):
        return self.available_occasions.append(available_occasion)





