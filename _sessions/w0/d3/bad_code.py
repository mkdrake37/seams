#!/usr/bin/python
from math import radians, cos, sin, asin, sqrt
from random import random, shuffle
from collections import defaultdict, OrderedDict
from sys import exit
from copy import deepcopy
from stuff import *
pixel_size = 0.00416667
min_x_center = -90.40409499
min_y_center = 19.72078911
workplace_neighborhood = 1000 
student_teacher_ratio = 28
work_codes   = [110, 112, 113, 116, 120]
home_codes   = [114, 200, 310, 320, 340, 390, 999]
school_codes = [111, 330]
child_code   = 0
school_age   = 5
field_idx = dict(zip('hid age sex x y workid hh_serial pernum day_loc'.split(), range(9)))
hh_loc = dict()
header = True
for line in file('locations-yucatan.txt'):
    if header:
        header = False
        continue
    p = line.split()
    if p[1] != 'house':
        exit()
    hh_loc[int(p[0])] = {'x':float(p[2]), 'y':float(p[3])}
workplaces_and_schools = []
max_loc_id = max(hh_loc.keys())
current_max_loc_id = max_loc_id
header = True
loc_id = current_max_loc_id + 1
total_raw_workers = 0
workplace_lookup = dict()
for line in file(filename):
    if header:
        header = False
        continue
    p = line.split()
    w = {'workid':loc_id, 'type':p[0].lower(), 'x':float(p[2]), 'y':float(p[3]), 'workers':0, 'students':0}
    if w['type'] == 'w':
        w['raw_workers'] = int(p[1])
        total_raw_workers += w['raw_workers']
    else:
        w['raw_workers'] = 0
    w['xi'] = x_to_col_num(w['x'])
    w['yi'] = y_to_row_num(w['y'])
    workplaces_and_schools.append(w)
    workplace_lookup[w['workid']] = len(workplaces_and_schools) - 1
    loc_id += 1
workplaces_and_schools.sort(cmp=xy_cmp)
pop = OrderedDict()
pop_ids = []
day_loc_ctr = {'h':0, 'w':0, 's':0} # home / work / school
filename = 'population-yucatan.txt'
header = True
i = -1 
for line in file('population-yucatan.txt'):
    i += 1
    if header:
        header = False
        continue
    p = map(int, line.split())
    hid = p[1]
    age = p[2]
    code = p[9]
    code = int(code)
    loc = ''
    if code in school_codes or (code == 0 and age >= school_age):
        loc = 's'
    elif code in work_codes:
        loc = 'w'
    elif code in home_codes or (code == 0 and age < school_age):
        loc = 'h'
    else:
        print "Error: encountered bad employment (EMPSTATD) code:", code
        exit()
    day_loc = loc
    day_loc_ctr[day_loc] += 1
    pop[p[0]] = p[1:4] + [hh_loc[hid]['x'], hh_loc[hid]['y'], -1, p[7], p[8], day_loc]
    pop_ids.append(p[0])
print "Total number of non-teacher jobs (DENUE):", total_raw_workers
print "Student:Teacher ratio (World Bank):", student_teacher_ratio
print "Total number of needed teachers:", day_loc_ctr['s']/student_teacher_ratio
print "Total raw number of jobs (DENUE + needed teachers):", total_raw_workers + day_loc_ctr['s']/student_teacher_ratio
shuffle(pop_ids)
students_allocated = 0
for pid in pop_ids:
    loc_type = pop[pid][field_idx['day_loc']]
    if loc_type != 's':
        continue
    num_loc_needed = 1
    px, py = pop[pid][field_idx['x']], pop[pid][field_idx['y']]
    pxi, pyi = x_to_col_num(px), y_to_row_num(py)
    commute_range = -1
    positions_found = 0
    nearby_places = [] # by index in workplaces_and_schools
    if loc_type == 'w':
        pos_type = 'workers'
    else:
        pos_type = 'students'
    while (len(nearby_places) < num_loc_needed and len(nearby_places) < len(workplaces_and_schools)) or (positions_found <= 0):
        nearby_places = []
        commute_range += 1
        for x_val in range(pxi-commute_range, pxi+commute_range+1):
            pos_xmin = binary_search(workplaces_and_schools, x_val, dict_val_lt, dict_val_gt, dict_val_eq, 'xi', 'lower')
            pos_xmax = binary_search(workplaces_and_schools, x_val+1, dict_val_lt, dict_val_gt, dict_val_eq, 'xi', 'upper')
            if pos_xmin == pos_xmax:
                continue
            pos_ymin = binary_search(workplaces_and_schools[pos_xmin:pos_xmax], pyi-commute_range, dict_val_lt, dict_val_gt, dict_val_eq, 'yi', 'lower')
            pos_ymax = binary_search(workplaces_and_schools[pos_xmin:pos_xmax], pyi+commute_range+1, dict_val_lt, dict_val_gt, dict_val_eq, 'yi', 'upper')
            for i,w in enumerate(workplaces_and_schools[pos_xmin:pos_xmax][pos_ymin:pos_ymax]):
                if pos_type == 'students':
                    positions_found += 1
                    nearby_places.append(w['workid'])
                elif w[pos_type] > 0:
                        positions_found += w[pos_type]
                        nearby_places.append(w['workid'])
    closest_school, min_dist = workplaces_and_schools[workplace_lookup[nearby_places[0]]], () # () evaluates to greater than any number
    for workid in nearby_places:
        s = workplaces_and_schools[workplace_lookup[workid]]
        d = haversine(px, py, s['x'], s['y'])
        if d < min_dist:
            min_dist = d
            closest_school = s
    school, distance = closest_school, min_dist
    pop[pid][field_idx['workid']] = school['workid'] 
    school['students'] += 1
    school['raw_workers'] += 1.0/student_teacher_ratio
    total_raw_workers     += 1.0/student_teacher_ratio
    students_allocated += 1
    if students_allocated % 10000 == 0:
        print "students sent to school:", students_allocated
employment_rescaling_factor = day_loc_ctr['w'] / float(total_raw_workers)
for place in workplaces_and_schools:
    place['workers'] = place['raw_workers'] * employment_rescaling_factor 
fo = file('population-yucatan_no_copy.txt','w')
fo.write('pid hid age sex hh_serial pernum workid\n')
W_AND_S_COPY = deepcopy(workplaces_and_schools)
ctr = 0 
for pid in pop.keys():
    person = pop[pid]
    loc_type = person[field_idx['day_loc']]
    if loc_type == 'h':
        person[field_idx['workid']] = person[field_idx['hid']]
    elif loc_type == 'w':
        px, py = person[field_idx['x']], person[field_idx['y']]
        pxi, pyi = x_to_col_num(px), y_to_row_num(py)
        nearby_places, positions_found = get_nearby_places(pxi, pyi, loc_type, workplaces_and_schools, workplace_neighborhood)
        raw_weights = [0.0 for i in range(len(nearby_places))]
        for i, workid in enumerate(nearby_places):
            w = workplaces_and_schools[workplace_lookup[workid]]
            dist = haversine(px, py, w['x'], w['y'])
            size = w['workers']
            raw_weights[i] = size / dist**2
        probs = []
        total = sum(raw_weights)
        for wt in raw_weights:
            probs.append(wt/total)
        r = random()
        for i,p in enumerate(probs):
            if r < p:
                return workplaces_and_schools[workplace_lookup[nearby_places[i]]]
            r -= p
        workplace = workplaces_and_schools[workplace_lookup[nearby_places[-1]]]
        workplace['workers'] -= 1
        if workplace['workers'] <= 0:
            for i,v in enumerate(workplaces_and_schools):
                if v['workid'] == workplace['workid']:
                    del workplaces_and_schools[i]
                    break
        person[field_idx['workid']] = workplace['workid']
    fo.write(' '.join(map(str,[
                       pid, 
                       person[field_idx['hid']],  
                       person[field_idx['age']],  
                       person[field_idx['sex']], 
                       person[field_idx['hh_serial']],
                       person[field_idx['pernum']],
                       person[field_idx['workid']],
                      ])) + '\n') 
    ctr += 1
    if ctr % 1000 == 0:
        print "placed", ctr, "people"
        print "workplace list size:", len(workplaces_and_schools)
fo.close()
