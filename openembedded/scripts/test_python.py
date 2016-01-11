#!/usr/bin/env python

import subprocess

<<<<<<< HEAD
print "Running a simple test"
=======
Print "Running a simple test"
>>>>>>> 871cf12cef08d83f4457283a120e47a2745a2a88
wget_command = "wget http://people.linaro.org/~timothy.anzaku/bb_black/zImage"
ret = subprocess.call(wget_command,shell=True)

if ret == 0:
	print "test: pass"
else:
	print "test: fail"
