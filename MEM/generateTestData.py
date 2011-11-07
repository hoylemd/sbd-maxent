import pickle
import sys

test = [
    (dict(a=1,b=0,c=1)), # unseen
    (dict(a=1,b=0,c=0)), # unseen
    (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
    (dict(a=0,b=1,c=0)), # seen 1 time, label=x
    ]

if len(sys.argv) == 2
	output = open(sys.agrv[1], 'w')

	pickle.dump(test, output)

else:
	print "Usage: python generateTestData.py filename"
	print "    Where filename is the name of the file to dump testing data to."
