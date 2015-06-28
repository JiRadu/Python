#!/usr/bin/env python

#
# OSSS 2015: Simple Python script for finding out minimum and
# maximum grade in file
# Razvan Deaconescu, 2015
#

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)

    students = []
    for line in list(fp):
        tokens = line.strip().split('\t')
        student = {
                'first_name': tokens[0],
                'last_name': tokens[1],
                'group':tokens[2],
                'grade': int(tokens[3])
                }
        students.append(student)

    # Compute minimum grade in min_grade and max in max_grade.
    min_grade = 11
    max_grade = -1
    min_students = []
    max_students = []
    for s in students:
        if s['grade'] > max_grade:
            max_grade = s['grade']
            max_students = [s]
        elif s['grade'] == max_grade:
            max_students.append(s)
        if s['grade'] < min_grade:
            min_grade = s['grade']
            min_students = [s]
        elif s['grade'] == min_grade:
            min_students.append(s)

    print "Min grade is:", min_grade
    print "Min grade students:"
    for s in min_students:
        print "  %s %s - %s" % (s['first_name'], s['last_name'], s['group'])

    print "\nMax grade is:", max_grade
    print "Max grade students:"
    for s in max_students:
        print "  %s %s - %s" % (s['first_name'], s['last_name'], s['group'])

if __name__ == "__main__":
    sys.exit(main())
    