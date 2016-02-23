
#with open('log','rU') as f:
#	for line in f.readline():
#		print line
#		import pprint
#		pp=pprint.PrettyPrinter()
#		pp.pprint(line)
#f.close()

f= open('logfile','r')	
for line in f.read().split('\r'):
	print line
f.close()
