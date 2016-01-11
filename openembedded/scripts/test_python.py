#!/usr/bin/env python

import subprocess

print "Running a simple test"
wget_command = "wget http://people.linaro.org/~timothy.anzaku/bb_black/zImage"
ret = subprocess.call(wget_command,shell=True)

if ret == 0:
	print "test: pass"
else:
	print "test: fail"
