#!/usr/bin/env python

#with open('log','rU') as f:
#	for line in f.readline():
#		print line
#		import pprint
#		pp=pprint.PrettyPrinter()
#		pp.pprint(line)
#f.close()
import pprint
f= open('logfile','r')	
#for line in f.read().split('\r'):
for line in f.read():
	pp = pprint.PrettyPrinter()
	pp.pprint(line)
	#print line
f.close()
