#!/usr/bin/env python3

import caesar_utils as cu
from sys import argv

if not cu.argv_is_valid(argv):
    cu.remind_user_of_usage()
    exit(1)
