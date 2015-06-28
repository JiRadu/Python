#!/usr/bin/env python

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
                'group': tokens[2],
                'grade': int(tokens[3])
                }
        students.append(student)

if __name__ == "__main__":
    sys.exit(main())
