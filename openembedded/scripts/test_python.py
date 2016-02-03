#!/usr/bin/env python

import subprocess

print "Running a simple test"
#wget_command = "wget http://people.linaro.org/~timothy.anzaku/bb_black/zImage"
#ret = subprocess.call(wget_command,shell=True)

#if ret == 0:
#	print "test: pass"
#else:
#	print "test: fail"

# First attempt -- just read to stdout
#f = open('output_test.log', 'r')
#print f.read()
#f.close()


# Second Attempt -- Run similar commands as in the 
# first case but in a subprocess

with open('logfile') as file:
    header = file.readline()
    rc = subprocess.call(['cat'], stdin=file)
file.close()
print "End of test"
