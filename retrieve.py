#!/usr/bin/env python3
# coding=<utf-8>


import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Database name")
parser.add_argument("path", help="Path to the pg_dumpall file")
args = parser.parse_args()
dirname = os.path.dirname(args.path)
with open(args.path) as dumpall, open('{}/dump_{}'.format(dirname, args.name), 'w') as dumpdb:
    copy = False
    for line in dumpall:
        if line.strip() == "\connect {}".format(args.name):
            copy = True
        elif line.strip() == "-- PostgreSQL database dump complete":
            copy = False
        elif copy:
            dumpdb.write(line)
