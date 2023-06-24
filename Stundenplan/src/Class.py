class Class:

    def __init__(self, class_id, class_name): #evtl noch eine Liste mit allen Anlässen?
        self._class_id = class_id
        self._class_name = class_name
        self._timeframes = {'Mon':[0, 0, 0, 0], 'Tue':[0, 0, 0, 0], 'Wed':[0, 0, 0, 0], 'Thu':[0, 0, 0, 0], 'Fri':[0, 0, 0, 0], 'Sat':[0, 0]}

    @property
    def class_id(self):
        return self._class_id

    @property
    def class_name(self):
        return self._class_name

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







