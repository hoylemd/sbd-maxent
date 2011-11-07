import pickle
import sys

train = [
	(dict(a=1,b=1,c=1), 'y'),
    (dict(a=1,b=1,c=1), 'x'),
    (dict(a=1,b=1,c=0), 'y'),
    (dict(a=0,b=1,c=1), 'x'),
    (dict(a=0,b=1,c=1), 'y'),
    (dict(a=0,b=0,c=1), 'y'),
    (dict(a=0,b=1,c=0), 'x'),
    (dict(a=0,b=0,c=0), 'x'),
    (dict(a=0,b=1,c=1), 'y'),
	]

if len(sys.argv) == 2:
	output = open(sys.argv[1], 'w')

	pickle.dump(train, output)

else:
	print "Usage: python generateTrainData.py filename"
	print "    Where filename is the name of the file to dump training data to."
