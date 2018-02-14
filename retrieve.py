#!/usr/bin/env python3
# coding=<utf-8>


import os

print("Enter path to dump:", end=" ")
dump = input()
dirname = os.path.dirname(dump)
print("Enter dbname:", end=" ")
name = input()
with open(dump) as dumpall, open('{}/dump_{}'.format(dirname,
                                 name), 'w') as dumpdb:
    copy = False
    for line in dumpall:
        if line.strip() == "\connect {}".format(name):
            copy = True
        elif line.strip() == "-- PostgreSQL database dump complete":
            copy = False
        elif copy:
            dumpdb.write(line)
