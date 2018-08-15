#!/usr/bin/python

import crypt, getpass, sys;

def print_hash(passwd):
	print(crypt.crypt(passwd, crypt.mksalt(crypt.METHOD_SHA512)))


if sys.stdin.isatty():
	print_hash(getpass.getpass())
else:
	for line in sys.stdin:
            print_hash(line)
