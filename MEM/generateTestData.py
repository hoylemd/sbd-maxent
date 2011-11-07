import pickle
import sys

test = [
    (dict(a=1,b=0,c=1,d=1)), # seen once, label x
    (dict(a=1,b=0,c=0,d=0)), # unseen
	(dict(a=1,b=0,c=0,d=0)), # unseen, should be same as last
    (dict(a=0,b=1,c=1,d=1)), # seen twice, labels=x,y
    (dict(a=0,b=1,c=0,d=0)), # seen 1 time, label=x
	(dict(a=0,b=0,c=0,d=0)), #seen 5 times, labels=y,y,y,x,y 
    ]

if len(sys.argv) == 2:
	output = open(sys.argv[1], 'w')

	pickle.dump(test, output)

else:
	print "Usage: python generateTestData.py filename"
	print "    Where filename is the name of the file to dump testing data to."
