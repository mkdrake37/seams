__author__ = 'carlpearson'

import csv

def seeds():
    res = []
    with open("rdat.csv", newline="") as csvfile:
        lines_reader = csv.reader(csvfile)
        lines_reader.__next__()
        for x in range(0, 5):
            dat = lines_reader.__next__()
            res.append(int(dat[1].strip()))
    return res

def color_list():
    res = []
    with open("cdat.csv", newline="") as csvfile:
        lines_reader = csv.reader(csvfile)
        lines_reader.__next__()
        for x in range(0, 3):
            dat = lines_reader.__next__()
            res.append(dat[1].strip())
    return res

def shape_list():
    res = []
    with open("sdat.csv", newline="") as csvfile:
        lines_reader = csv.reader(csvfile)
        lines_reader.__next__()
        for x in range(0, 3):
            dat = lines_reader.__next__()
            res.append(dat[1].strip())
    return res

import random

colors = color_list()
shapes = shape_list()

for s in seeds():
    random.seed(s)
    print("seed", s, sep=" ")
    with open("cuts"+str(s)+".out", mode="w") as tarfile:
        writer = csv.writer(tarfile)
        res = {}
        for x in range(0, 30):
            c = random.choice(colors)
            s = random.choice(shapes)
            writer.writerow([c, s])
            m = res.get(c, {})
            m[s] = m.get(s, 0) + 1
            res[c] = m
        print(res)
