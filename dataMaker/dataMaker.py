import sys

if len(sys.argv) == 2:
	f = open(sys.argv[1], 'r')

	contexts = f.readlines()

	for line in contexts:
		print line

else:
	print "Usage: python dataMaker <filename>"
	print "    where <filename> is the path to a contexts file"
