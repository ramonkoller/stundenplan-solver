class Penalty:

    def __init__(self, penalty_name, penalty_value):
        self._penalty_name = penalty_name
        self._penalty_value = penalty_value

    @property
    def penalty_name(self):
        return self._penalty_name

    @property
    def penalty_value(self):
        return self._penalty_value


class PenaltyAllBlocksPlanned(Penalty):

    def __init__(self, penalty_value, occasion_name, block):
        Penalty.__init__(self, "block_nicht_verplant", penalty_value)
        self._occasion_name = occasion_name
        self._block = block

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def block(self):
        return self._block

    def to_json(self):
        return {"modul": self.occasion_name, "block": str(self.block), "penalty": str(self.penalty_value)}


class PenaltyLecturesCollision(Penalty):

    def __init__(self, penalty_value, lecture_name, day, slot):
        Penalty.__init__(self, "dozenten_kollision", penalty_value)
        self._lecture_name = lecture_name
        self._day = day
        self._slot = slot

    @property
    def lecture_name(self):
        return self._lecture_name

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    def to_json(self):
        return {"dozent": self.lecture_name, "tag": self.day, "slot": str(self.slot), "penalty": str(self.penalty_value)}


class PenaltyClassesCollision(Penalty):

    def __init__(self, penalty_value, class_name, day, slot):
        Penalty.__init__(self, "klassen_kollision", penalty_value)
        self._class_name = class_name
        self._day = day
        self._slot = slot

    @property
    def class_name(self):
        return self._class_name

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    def to_json(self):
        return {"klasse": self.class_name, "tag": self.day, "slot": str(self.slot), "penalty": str(self.penalty_value)}


class PenaltyRoomsCollision(Penalty):

    def __init__(self, penalty_value, room_name, day, slot):
        Penalty.__init__(self, "raum_kollision", penalty_value)
        self._room_name = room_name
        self._day = day
        self._slot = slot

    @property
    def room_name(self):
        return self._room_name

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    def to_json(self):
        return {"raum": self.room_name, "tag": self.day, "slot": str(self.slot), "penalty": str(self.penalty_value)}


class PenaltyRoomsCapacity(Penalty):

    def __init__(self, penalty_value, occasion_name, block, room_name):
        Penalty.__init__(self, "raum_keine_kapazitaet", penalty_value)
        self._occasion_name = occasion_name
        self._block = block
        self._room_name = room_name

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def block(self):
        return self._block

    @property
    def room_name(self):
        return self._room_name

    def to_json(self):
        return {"modul": self.occasion_name, "block": str(self.block), "raum": self.room_name, "penalty": str(self.penalty_value)}


class PenaltyOneBlockPerDay(Penalty):

    def __init__(self, penalty_value, occasion_name, day):
        Penalty.__init__(self, "mehr_als_ein_Block_pro_Tag", penalty_value)
        self._occasion_name = occasion_name
        self._day = day

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def day(self):
        return self._day

    def to_json(self):
        return {"modul": self.occasion_name, "tag": self.day, "penalty": str(self.penalty_value)}


class PenaltyClassesCompact(Penalty):

    def __init__(self, penalty_value, class_name, day):
        Penalty.__init__(self, "klasse_unterrichtsluecke", penalty_value)
        self._class_name = class_name
        self._day = day

    @property
    def class_name(self):
        return self._class_name

    @property
    def day(self):
        return self._day

    def to_json(self):
        return {"klasse": self.class_name, "tag": self.day, "penalty": str(self.penalty_value)}


class PenaltyLecturesCompact(Penalty):

    def __init__(self, penalty_value, lecture_name, day):
        Penalty.__init__(self, "dozent_unterrichtsluecke", penalty_value)
        self._lecture_name = lecture_name
        self._day = day

    @property
    def lecture_name(self):
        return self._lecture_name

    @property
    def day(self):
        return self._day

    def to_json(self):
        return {"dozent": self.lecture_name, "tag": self.day, "penalty": str(self.penalty_value)}


class PenaltyClassesPriorities(Penalty):

    def __init__(self, penalty_value, class_name, day, slot):
        Penalty.__init__(self, "klasse_schlechter_zeitpunkt", penalty_value)
        self._class_name = class_name
        self._day = day
        self._slot = slot

    @property
    def class_name(self):
        return self._class_name

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    def to_json(self):
        return {"klasse": self.class_name, "tag": self.day, "slot": str(self.slot), "penalty": str(self.penalty_value)}


class PenaltyLecturesPriorities(Penalty):

    def __init__(self, penalty_value, lecture_name, day, slot):
        Penalty.__init__(self, "dozent_schlechter_zeitpunkt", penalty_value)
        self._lecture_name = lecture_name
        self._day = day
        self._slot = slot

    @property
    def lecture_name(self):
        return self._lecture_name

    @property
    def day(self):
        return self._day

    @property
    def slot(self):
        return self._slot

    def to_json(self):
        return {"dozent": self.lecture_name, "tag": self.day, "slot": str(self.slot), "penalty": str(self.penalty_value)}


class PenaltyEveningSaturdaySchool(Penalty):

    def __init__(self, penalty_value, occasion_name, day):
        Penalty.__init__(self, "block_am_abend_oder_samstag", penalty_value)
        self._occasion_name = occasion_name
        self._day = day

    @property
    def occasion_name(self):
        return self._occasion_name

    @property
    def day(self):
        return self._day

    def to_json(self):
        return {"modul": self.occasion_name, "tag": self.day, "penalty": str(self.penalty_value)}

