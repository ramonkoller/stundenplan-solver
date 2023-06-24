class Lecturer:

    def __init__(self, lecturer_id, lecturer_name):
        self._lecturer_id = lecturer_id
        self._lecturer_name = lecturer_name
        self._timeframes = {'Mon':[0, 0, 0, 0], 'Tue':[0, 0, 0, 0], 'Wed':[0, 0, 0, 0], 'Thu':[0, 0, 0, 0], 'Fri':[0, 0, 0, 0], 'Sat':[0, 0]}

    @property
    def lecturer_id(self):
        return self._lecturer_id

    @property
    def lecturer_name(self):
        return self._lecturer_name

    @property
    def timeframes(self):
        return self._timeframes

    def add_monday(self, list):
        self.timeframes['Mon'] = list

    def add_tuesday(self, list):
        self.timeframes['Tue'] = list

    def add_wednesday(self, list):
        self.timeframes['Wed'] = list

    def add_thursday(self, list):
        self.timeframes['Thu'] = list

    def add_friday(self, list):
        self.timeframes['Fri'] = list

    def add_saturday(self, list):
        self.timeframes['Sat'] = list
