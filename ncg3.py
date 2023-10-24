#!/usr/bin/env python3
import sys
import os

def generate_usernames(name):
    tokens = name.lower().split()
    if len(tokens) < 2:
        return
    fname = tokens[0]
    lname = tokens[-1]
    if len(tokens) == 3:
        mname = tokens[1]
        print(fname[0] + mname[0] + lname)
        print(fname[0] + mname + lname)
        print(fname + mname[0] + lname)
        print(fname + "." + mname + "." + lname)
    print(fname + lname)
    print(lname + fname)
    print(fname + "." + lname)
    print(lname + "." + fname)
    print(lname + fname[0])
    print(fname[0] + lname)
    print(lname[0] + fname)
    print(fname[0] + "." + lname)
    print(lname[0] + "." + fname)
    print(fname)
    print(lname)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: {} names.txt".format(sys.argv[0]))
        sys.exit(0)
    if not os.path.exists(sys.argv[1]):
        print("{} not found".format(sys.argv[1]))
        sys.exit(0)
    with open(sys.argv[1], 'r') as f:
        for line in f:
            name = ''.join([c for c in line if c == " " or c.isalpha()])
            generate_usernames(name)
