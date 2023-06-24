import json
from datetime import datetime
import xlsxwriter


class ProblemBack:

    def __init__(self, problem_back_id, problem_back_name, overall_penalty_value, problem, schedule_number):
        self._problem_back_id = problem_back_id
        self._problem_back_name = problem_back_name
        self._overall_penalty_value = overall_penalty_value
        self._problem = problem
        self._schedule_number = schedule_number
        self._datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._scheduled_occasions = []
        self._scheduled_lectures = {}
        self._scheduled_classes = {}
        self._scheduled_rooms = {}
        self._scheduled_penalties = []

    @property
    def problem_back_id(self):
        return self._problem_back_id

    @property
    def problem_back_name(self):
        return self._problem_back_name

    @property
    def overall_penalty_value(self):
        return self._overall_penalty_value

    @property
    def problem(self):
        return self._problem

    @property
    def schedule_number(self):
        return self._schedule_number

    @property
    def datum(self):
        return self._datum

    @property
    def scheduled_occasions(self):
        return self._scheduled_occasions

    @property
    def scheduled_lectures(self):
        return self._scheduled_lectures

    @property
    def scheduled_classes(self):
        return self._scheduled_classes

    @property
    def scheduled_rooms(self):
        return self._scheduled_rooms

    @property
    def scheduled_penalties(self):
        return self._scheduled_penalties

    def add_scheduled_occasion(self, scheduled_occasion):
        self.scheduled_occasions.append(scheduled_occasion)

    def add_lectures_occasion(self, lectures_name, occasion_name, block, day, slot, room_nr, lecture_priority):
        string = day, slot, occasion_name, block, room_nr, "[Priority: ", lecture_priority, "]"
        if lectures_name in self.scheduled_lectures.keys():
            self.scheduled_lectures[lectures_name].append(string)
        else:
            self.scheduled_lectures[lectures_name] = [string]

    def add_classes_occasion(self, class_name, occasion_name, block, day, slot, room_nr, class_priority):
        string = day, slot, occasion_name, block, room_nr, "[Priority: ", class_priority, "]"
        if class_name in self.scheduled_classes.keys():
            self.scheduled_classes[class_name].append(string)
        else:
            self.scheduled_classes[class_name] = [string]

    def add_rooms_occasion(self, occasion_name, block, day, slot, room_nr, free_places):
        string = day, slot, occasion_name, block, free_places
        if room_nr in self.scheduled_rooms.keys():
            self.scheduled_rooms[room_nr].append(string)
        else:
            self.scheduled_rooms[room_nr] = [string]

    def add_penalty(self, penalty):
        self.scheduled_penalties.append(penalty)

    def create_scheduled_occasions_json(self):
        module_dict = dict()
        occasions_dict = dict()
        occasions_dict["id"] = self._problem_back_id
        occasions_dict["name"] = self._problem_back_name
        occasions_dict["gesamtpenalty"] = self.overall_penalty_value
        occasions_dict["datum"] = self.datum
        for o in self.scheduled_occasions:
            if o.occasion_name in module_dict.keys():
                module_dict[o.occasion_name]["bloecke"].append({"zeitslot": [self.transform_day_name_to_number(o.day), o.slot + 1], "raum": o.room_nr})
            else:
                module_dict[o.occasion_name] = dict()
                module_dict[o.occasion_name]["bloecke"] = [{"zeitslot": [self.transform_day_name_to_number(o.day), o.slot + 1], "raum": o.room_nr}]
        occasions_dict["module"] = module_dict
        occasions_json = json.dumps(occasions_dict)
        with open("C:/Users/ramon.koller/Documents/BachelorAIML/3Semester/IIP/IDMS_Zugang/idms-iip-02/IDMSAdmin/wwwroot/json/occasions/Scheduled_occasions_" + self.schedule_number + ".json", "w") as outfile:
            outfile.write(occasions_json)
        print("schedulded_occasions_" + self.schedule_number + ".json was written")

    def create_scheduled_penalties_json(self):
        penalties_dict = dict()
        full_penalties_dict = dict()
        full_penalties_dict["id"] = self.problem_back_id
        full_penalties_dict["name"] = self.problem_back_name
        full_penalties_dict["gesamtpenalty"] = self.overall_penalty_value
        full_penalties_dict["datum"] = self.datum
        for p in self.scheduled_penalties:
            if p.penalty_name in penalties_dict.keys():
                penalties_dict[p.penalty_name].append(p.to_json())
            else:
                penalties_dict[p.penalty_name] = [p.to_json()]
        full_penalties_dict["penalties"] = penalties_dict
        penalties_json = json.dumps(full_penalties_dict)
        with open("C:/Users/ramon.koller/Documents/BachelorAIML/3Semester/IIP/IDMS_Zugang/idms-iip-02/IDMSAdmin/wwwroot/json/penalties/scheduled_penalties_" + self.schedule_number + ".json", "w") as outfile:
            outfile.write(penalties_json)
        print("schedulded_penalties_" + self.schedule_number + ".json was written")

    def create_scheduled_rooms_excel(self):
        workbook = xlsxwriter.Workbook("../output_data/scheduled_rooms_" + self.schedule_number + ".xlsx")
        bold = workbook.add_format({'bold': True})
        align_left = workbook.add_format({'align': 'left'})

        information = workbook.add_worksheet("Allgemeine Informationen")
        information.write('A1', 'Stundenplan-ID:', bold)
        information.write('A2', 'Stundenplan-Name:', bold)
        information.write('A3', 'Gesamtpenaltywert:', bold)
        information.write('A4', 'Datum:', bold)
        information.write('B1', self.problem_back_id, align_left)
        information.write('B2', self.problem_back_name, align_left)
        information.write('B3', self.overall_penalty_value, align_left)
        information.write('B4', self.datum, align_left)
        information.set_column(1, 5, 25)

        for r in self.problem.rooms:
            room_sheet = workbook.add_worksheet(r.room_nr)
            self.draw_timetable(room_sheet, bold)
            for so in self.scheduled_occasions:
                if so.room_nr == r.room_nr:
                    self.timetable_add_occasion(room_sheet, so.occasion_name, so.day, so.slot, so.room_nr)
            room_sheet.set_column(1, 20, 25)
        print("schedulded_rooms_" + self.schedule_number + ".xlsx was written")
        workbook.close()

    def create_scheduled_classes_excel(self):
        workbook = xlsxwriter.Workbook("../output_data/scheduled_classes_" + self.schedule_number + ".xlsx")
        bold = workbook.add_format({'bold': True})
        align_left = workbook.add_format({'align': 'left'})

        information = workbook.add_worksheet("Allgemeine Informationen")
        information.write('A1', 'Stundenplan-ID:', bold)
        information.write('A2', 'Stundenplan-Name:', bold)
        information.write('A3', 'Gesamtpenaltywert:', bold)
        information.write('A4', 'Datum:', bold)
        information.write('B1', self.problem_back_id, align_left)
        information.write('B2', self.problem_back_name, align_left)
        information.write('B3', self.overall_penalty_value, align_left)
        information.write('B4', self.datum, align_left)
        information.set_column(1, 5, 25)

        for c in self.problem.classes:
            class_sheet = workbook.add_worksheet(c.class_name)
            self.draw_timetable(class_sheet, bold)
            for o in self.problem.occasions:
                if c.class_name in o.classes_names and o.module_type in ["K", "M", "P"]:
                    for so in self.scheduled_occasions:
                        if so.occasion_name == o.occasion_name:
                            self.timetable_add_occasion(class_sheet, so.occasion_name, so.day, so.slot, so.room_nr)
            class_sheet.set_column(1, 20, 25)
        print("schedulded_classes_" + self.schedule_number + ".xlsx was written")
        workbook.close()

    def create_scheduled_lecturers_excel(self):
        workbook = xlsxwriter.Workbook("../output_data/scheduled_lecturers_" + self.schedule_number + ".xlsx")
        bold = workbook.add_format({'bold': True})
        align_left = workbook.add_format({'align': 'left'})

        information = workbook.add_worksheet("Allgemeine Informationen")
        information.write('A1', 'Stundenplan-ID:', bold)
        information.write('A2', 'Stundenplan-Name:', bold)
        information.write('A3', 'Gesamtpenaltywert:', bold)
        information.write('A4', 'Datum:', bold)
        information.write('B1', self.problem_back_id, align_left)
        information.write('B2', self.problem_back_name, align_left)
        information.write('B3', self.overall_penalty_value, align_left)
        information.write('B4', self.datum, align_left)
        information.set_column(1, 5, 25)

        for l in self.problem.lecturers:
            lecturer_sheet = workbook.add_worksheet(l.lecturer_name)
            self.draw_timetable(lecturer_sheet, bold)
            for o in self.problem.occasions:
                if l.lecturer_id in o.lecturers_id:
                    for so in self.scheduled_occasions:
                        if so.occasion_name == o.occasion_name:
                            self.timetable_add_occasion(lecturer_sheet, so.occasion_name, so.day, so.slot, so.room_nr)
            lecturer_sheet.set_column(1, 20, 25)
        print("schedulded_lecturers_" + self.schedule_number + ".xlsx was written")
        workbook.close()

    def draw_timetable(self, sheet, bold):
        sheet.write('B2', 'Stundenplan', bold)
        sheet.write('B4', 'Zeit:', bold)
        sheet.write('C4', 'Montag:', bold)
        sheet.write('D4', 'Dienstag:', bold)
        sheet.write('E4', 'Mittwoch:', bold)
        sheet.write('F4', 'Donnerstag:', bold)
        sheet.write('G4', 'Freitag:', bold)
        sheet.write('H4', 'Samstag:', bold)
        sheet.write('B5', '9:05 - 11:25:', bold)
        sheet.write('B6', '12:50 - 15:10:', bold)
        sheet.write('B7', '15:30 - 17:50:', bold)
        sheet.write('B8', '18:30 - 20:50:', bold)

    def timetable_add_occasion(self, sheet, occasion_name, day, slot, room_nr):
        if day == "Mon":
            column = "C"
        elif day == "Tue":
            column = "D"
        elif day == "Wed":
            column = "E"
        elif day == "Thu":
            column = "F"
        elif day == "Fri":
            column = "G"
        elif day == "Sat":
            column = "H"
        else:
            column = "K"

        if slot == 0:
            row = 5
        elif slot == 1:
            row = 6
        elif slot == 2:
            row = 7
        elif slot == 3:
            row = 8
        else:
            row = 10

        sheet.write(column + str(row), occasion_name + "; " + room_nr)

    def transform_day_name_to_number(self, number):
        if number == "Mon":
            return 1
        elif number == "Tue":
            return 2
        elif number == "Wed":
            return 3
        elif number == "Thu":
            return 4
        elif number == "Fri":
            return 5
        elif number == "Sat":
            return 6


