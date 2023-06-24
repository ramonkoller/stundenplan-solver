import json
from datetime import datetime

from conda_build.utils import tar_xf
import sys
from Class import Class
from Constraint_All_Blocks_Planned import ConstraintAllBlocksPlanned
from Constraint_Block_Per_Day import ConstraintBlockPerDay
from Constraint_Blocks_Planned_fix import ConstraintBlocksPlannedFix
from Constraint_Classes_Collisions import ConstraintClassesCollisions
from Constraint_Classes_Compact import ConstraintClassesCompact
from Constraint_Classes_Priorities import ConstraintClassesPriorities
from Constraint_Evening_Saturday_School import ConstraintEveningSaturdaySchool
from Constraint_Lecturer_Compact import ConstraintLecturersCompact
from Constraint_Lecturers_Collisions import ConstraintLecturersCollisions
from Constraint_Lecturers_Priorities import ConstraintLecturersPriorities
from Constraint_Rooms_Capacity import ConstraintRoomsCapacity
from Constraint_Rooms_Collisions import ConstraintRoomsCollisions
from Constraint_Rooms_Planned_fix import ConstraintRoomsPlannedFix
from Lecturer import Lecturer
from Occasion import Occasion
from Penalty import Penalty, PenaltyAllBlocksPlanned, PenaltyLecturesCollision, PenaltyClassesCollision, \
    PenaltyRoomsCollision, PenaltyRoomsCapacity, PenaltyOneBlockPerDay, PenaltyClassesCompact, PenaltyLecturesCompact, \
    PenaltyLecturesPriorities, PenaltyClassesPriorities, PenaltyEveningSaturdaySchool
from Problem import Problem
from Problem_Back import ProblemBack
from Room import Room
from Scheduled_Occasions import ScheduledOccasion


def run_solver(semester, occasions, lecturers, classes, rooms, penalties):

    standard_output = sys.stdout
    with open('../input_data/schedule_number.txt', 'r') as txt_file:
        schedule_number = txt_file.read()

    with open('../input_data/schedule_number.txt', 'w') as txt_file:
        txt_file.write(str(int(schedule_number) + 1))

    sys.stdout = open('../output_data/log_output_' + schedule_number + '.txt', 'w')

    all_blocks_planned_fix = penalties['all_blocks_planned_fix']
    all_blocks_planned_penalty = penalties['all_blocks_planned_penalty']
    lectures_collisions_fix = penalties['lectures_collisions_fix']
    lectures_collisions_penalty = penalties['lectures_collisions_penalty']
    classes_collisions_fix = penalties['classes_collisions_fix']
    classes_collisions_penalty = penalties['classes_collisions_penalty']
    rooms_collisions_fix = penalties['rooms_collisions_fix']
    rooms_collisions_penalty = penalties['rooms_collisions_penalty']

    lectures_priorities_fix = penalties['lectures_priorities_fix']
    lectures_priorities_penalty_list = penalties['lectures_priorities_penalty_list']
    classes_priorities_fix = penalties['classes_priorities_fix']
    classes_priorities_penalty_list = penalties['classes_priorities_penalty_list']

    one_block_per_day_fix = penalties['one_block_per_day_fix']
    one_block_per_day_penalty = penalties['one_block_per_day_penalty']

    classes_compact_penalty = penalties['classes_compact_penalty']
    lectures_compact_penalty = penalties['lectures_compact_penalty']
    evening_saturday_school_penalty = penalties['evening_saturday_school_penalty']

    problem = Problem("Stundenplan_" + str(schedule_number), semester[3]['ShortName'])

    for i in range(len(rooms)):
        if rooms[i]['Location']:
            if rooms[i]['Location']['Name'] != "Horw":
                problem.add_room(Room(rooms[i]['Id'], rooms[i]['RaumNr'], rooms[i]['Name'], rooms[i]['AnzPlaetzeUnt'],
                                      rooms[i]['Virtual']))
        else:
            problem.add_room(
                Room(rooms[i]['Id'], rooms[i]['RaumNr'], rooms[i]['Name'], rooms[i]['AnzPlaetzeUnt'], rooms[i]['Virtual']))
    print("rooms imported", datetime.now())

    for i in range(len(occasions)):
        occasion = Occasion(occasions[i]['Id'], occasions[i]['ModuleId'], occasions[i]['Name'],
                            occasions[i]['ModuleType'], occasions[i]['NumBlocksPerWeek'], occasions[i]['NumStudents'],
                            occasions[i]['HasFixedSchedule'], occasions[i]['BlocksPerOccasion'],
                            occasions[i]['ClassesPerOccasion'], occasions[i]['LecturersPerOccasion'],
                            occasions[i]['RoomId'])
        if occasion.rooms_id:
            for r in problem.rooms:
                if occasion.rooms_id == r.room_id:
                    occasion.add_available_room(r)
                    r.add_available_occasion(occasion)
        else:
            for r in problem.rooms:
                if occasion.num_students < r.capacity:
                    occasion.add_available_room(r)
                    r.add_available_occasion(occasion)
        problem.add_occasion(occasion)
    print("occasions imported", datetime.now())

    for i in range(len(lecturers)):
        lecturer = Lecturer(lecturers[i]['EmployeeId'], lecturers[i]['EmployeeName'])
        lecturer.add_monday(lecturers[i]['Timeframes'][0]['Priorities'])
        lecturer.add_tuesday(lecturers[i]['Timeframes'][1]['Priorities'])
        lecturer.add_wednesday(lecturers[i]['Timeframes'][2]['Priorities'])
        lecturer.add_thursday(lecturers[i]['Timeframes'][3]['Priorities'])
        lecturer.add_friday(lecturers[i]['Timeframes'][4]['Priorities'])
        lecturer.add_saturday(lecturers[i]['Timeframes'][5]['Priorities'])
        problem.add_lecture(lecturer)
        problem.lecturers_by_id[lecturers[i]['EmployeeId']] = lecturer
        problem.lecturer_ids.add(lecturers[i]['EmployeeId'])
    print("lecturers imported", datetime.now())

    for i in range(len(classes)):
        one_class = Class(classes[i]['Id'], classes[i]['Name'])
        one_class.add_monday(classes[i]['Timeframes'][0]['Priorities'])
        one_class.add_tuesday(classes[i]['Timeframes'][1]['Priorities'])
        one_class.add_wednesday(classes[i]['Timeframes'][2]['Priorities'])
        one_class.add_thursday(classes[i]['Timeframes'][3]['Priorities'])
        one_class.add_friday(classes[i]['Timeframes'][4]['Priorities'])
        one_class.add_saturday(classes[i]['Timeframes'][5]['Priorities'])
        problem.add_class(one_class)
        problem.classes_by_id[classes[i]['Id']] = one_class
        problem.classes_by_name[classes[i]['Name']] = one_class
        problem.class_ids.add(classes[i]['Id'])
        problem.class_names.add(classes[i]['Name'])
    print("classes imported", datetime.now())

    problem.add_solver_variables()

    ConstraintAllBlocksPlanned(problem, all_blocks_planned_penalty, all_blocks_planned_fix).add_constraint_to_model()
    ConstraintLecturersCollisions(problem, lectures_collisions_penalty, lectures_collisions_fix).add_constraint_to_model()
    ConstraintClassesCollisions(problem, classes_collisions_penalty, classes_collisions_fix).add_constraint_to_model()
    ConstraintRoomsCollisions(problem, rooms_collisions_penalty, rooms_collisions_fix).add_constraint_to_model()

    ConstraintBlocksPlannedFix(problem).add_constraint_to_model()
    ConstraintRoomsPlannedFix(problem).add_constraint_to_model()

    ConstraintLecturersPriorities(problem, lectures_priorities_penalty_list, lectures_priorities_fix).add_constraint_to_model()
    ConstraintClassesPriorities(problem, classes_priorities_penalty_list, classes_priorities_fix).add_constraint_to_model()

    ConstraintBlockPerDay(problem, one_block_per_day_penalty, one_block_per_day_fix).add_constraint_to_model()

    ConstraintClassesCompact(problem, classes_compact_penalty).add_constraint_to_model()
    ConstraintLecturersCompact(problem, lectures_compact_penalty).add_constraint_to_model()
    ConstraintEveningSaturdaySchool(problem, evening_saturday_school_penalty).add_constraint_to_model()

    problem.solve_problem()

    problem_back = ProblemBack(problem.problem_id, problem.problem_name, problem.objective.solution_value, problem, schedule_number)

    for o in problem.occasions:
        for b in range(o.blocks_per_week):
            for d in problem.days:
                for s in d.slots:
                    for r in o.available_rooms:
                        if problem.x[(o, b, d, s, r)].solution_value > 0.5:
                            problem_back.add_scheduled_occasion(ScheduledOccasion(o.occasion_name, b, d.day_name, s, r.room_nr))
                            problem_back.add_rooms_occasion(o.occasion_name, b, d.day_name, s, r.room_nr, r.capacity - o.num_students)

    for l in problem.lecturers:
        for o in problem.occasions:
            if l.lecturer_id in o.lecturers_id:
                for b in range(o.blocks_per_week):
                    for d in problem.days:
                        for s in d.slots:
                            for r in o.available_rooms:
                                if problem.x[(o, b, d, s, r)].solution_value > 0.5:
                                    problem_back.add_lectures_occasion(l.lecturer_name, o.occasion_name, b, d.day_name, s, r.room_nr, l.timeframes[d.day_name][s])
                                    if l.timeframes[d.day_name][s] == -1:
                                        problem_back.add_penalty(PenaltyLecturesPriorities(lectures_priorities_penalty_list[4], l.lecturer_name, d.day_name, s + 1))
                                    elif l.timeframes[d.day_name][s] == -2:
                                        problem_back.add_penalty(PenaltyLecturesPriorities(lectures_priorities_penalty_list[5], l.lecturer_name, d.day_name, s + 1))
                                    elif l.timeframes[d.day_name][s] == -3:
                                        problem_back.add_penalty(PenaltyLecturesPriorities(lectures_priorities_penalty_list[6], l.lecturer_name, d.day_name, s + 1))

    for c in problem.classes:
        for o in problem.occasions:
            if c.class_name in o.classes_names:
                for b in range(o.blocks_per_week):
                    for d in problem.days:
                        for s in d.slots:
                            for r in o.available_rooms:
                                if problem.x[(o, b, d, s, r)].solution_value > 0.5:
                                    problem_back.add_classes_occasion(c.class_name, o.occasion_name, b, d.day_name, s, r.room_nr, c.timeframes[d.day_name][s])
                                    if c.timeframes[d.day_name][s] == -1:
                                        problem_back.add_penalty(PenaltyClassesPriorities(classes_priorities_penalty_list[4], o.occasion_name, d.day_name, s + 1))
                                    elif c.timeframes[d.day_name][s] == -2:
                                        problem_back.add_penalty(PenaltyClassesPriorities(classes_priorities_penalty_list[5], o.occasion_name, d.day_name, s + 1))
                                    elif c.timeframes[d.day_name][s] == -3:
                                        problem_back.add_penalty(PenaltyClassesPriorities(classes_priorities_penalty_list[6], o.occasion_name, d.day_name, s + 1))

    print("Objective: " + str(problem.model.objective_value))

    if not all_blocks_planned_fix:
        for o in problem.occasions:
            for b in range(o.blocks_per_week):
                if problem.pob[(o, b)].solution_value > 0.5:
                    problem_back.add_penalty(PenaltyAllBlocksPlanned(all_blocks_planned_penalty, o.occasion_name, b))

    if not lectures_collisions_fix:
        for l in problem.lecturers:
            for d in problem.days:
                for s in d.slots:
                    if problem.pl[(l, d, s)].solution_value > 0.5:
                        problem_back.add_penalty(PenaltyLecturesCollision(lectures_collisions_penalty, l.lecturer_name, d.day_name, s + 1))

    if not classes_collisions_fix:
        for c in problem.classes:
            for d in problem.days:
                for s in d.slots:
                    if problem.pc[(c, d, s)].solution_value > 0.5:
                        problem_back.add_penalty(PenaltyClassesCollision(classes_collisions_penalty, c.class_name, d.day_name, s + 1))

    if not rooms_collisions_fix:
        for r in problem.rooms:
            if not r.virtual:
                for d in problem.days:
                    for s in d.slots:
                        if problem.pr[(r, d, s)].solution_value > 0.5:
                            problem_back.add_penalty(PenaltyRoomsCollision(rooms_collisions_penalty, r.room_nr, d.day_name, s + 1))

    if not one_block_per_day_fix:
        for o in problem.occasions:
            for d in problem.days:
                if problem.pbd[(o, d)].solution_value > 0.5:
                    problem_back.add_penalty(PenaltyOneBlockPerDay(one_block_per_day_penalty, o.occasion_name, d.day_name))

    for c in problem.classes:
        for d in problem.days:
            if problem.pcc[(c, d)].solution_value > 0.5:
                problem_back.add_penalty(PenaltyClassesCompact(classes_compact_penalty, c.class_name, d.day_name))

    for l in problem.lecturers:
        for d in problem.days:
            if problem.plc[(l, d)].solution_value > 0.5:
                problem_back.add_penalty(PenaltyLecturesCompact(lectures_compact_penalty, l.lecturer_name, d.day_name))

    for o in problem.occasions:
        for b in range(o.blocks_per_week):
            for d in problem.days:
                for r in o.available_rooms:
                    if d.day_name != "Sat":
                        if problem.x[(o, b, d, 3, r)].solution_value > 0.5:
                            problem_back.add_penalty(
                                PenaltyEveningSaturdaySchool(evening_saturday_school_penalty, o.occasion_name, d.day_name))

    for o in problem.occasions:
        for b in range(o.blocks_per_week):
            for d in problem.days:
                for s in d.slots:
                    for r in o.available_rooms:
                        if d.day_name == "Sat":
                            if problem.x[(o, b, d, s, r)].solution_value > 0.5:
                                problem_back.add_penalty(PenaltyEveningSaturdaySchool(evening_saturday_school_penalty, o.occasion_name, d.day_name))

    problem_back.create_scheduled_occasions_json()
    problem_back.create_scheduled_penalties_json()
    problem_back.create_scheduled_lecturers_excel()
    problem_back.create_scheduled_classes_excel()
    problem_back.create_scheduled_rooms_excel()

    sys.stdout.close()
    sys.stdout = standard_output
    return "solver has been finished"

