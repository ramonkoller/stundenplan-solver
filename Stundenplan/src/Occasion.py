class Occasion:

    def __init__(self, occasions_id, module_id, occasion_name, module_type, blocks_per_week, num_students, fix, fix_blocks,
                 classes_names, lecturers_id, room_id):
        self._occasions_id = occasions_id
        self._module_id = module_id
        self._occasion_name = occasion_name
        self._module_type = module_type
        self._blocks_per_week = blocks_per_week
        self._num_students = num_students
        self._fix = fix
        self._fix_blocks = fix_blocks
        self._classes_names = classes_names
        self._lecturers_id = lecturers_id
        self._rooms_id = room_id
        self._available_rooms = []

    @property
    def occasions_id(self):
        return self._occasions_id

    @property
    def module_id(self):
        return self._module_id

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def module_type(self):
        return self._module_type

    @property
    def blocks_per_week(self):
        return self._blocks_per_week

    @property
    def num_students(self):
        return self._num_students

    @property
    def fix(self):
        return self._fix

    @property
    def fix_blocks(self):
        return self._fix_blocks

    @property
    def classes_names(self):
        return self._classes_names

    @property
    def lecturers_id(self):
        return self._lecturers_id

    @property
    def rooms_id(self):
        return self._rooms_id

    @property
    def available_rooms(self):
        return self._available_rooms

    def add_available_room(self, available_room):
        return self.available_rooms.append(available_room)




