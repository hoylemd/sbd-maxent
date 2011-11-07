import nltk
import pickle
import sys

def test_maxent(model, data):
	print "in test_maxent"

	f = open("classdemo.model", 'r')
	
	if isinstance(model, Exception):
		print 'Error: %r' % model
	else:
		i = 1;
		for featureset in data:
			print "Test #%d:" % (i),
			i += 1
			pdist = model.prob_classify(featureset)
			label = model.classify(featureset)
			print 'x: %.2f y: %.2f descision: %s' % (pdist.prob('x'), pdist.prob('y'), label)


if len(sys.argv) == 3:
	modelFile = open(sys.argv[1], 'r')
	model = pickle.load(modelFile)

	dataFile = open(sys.argv[2], 'r')
	data = pickle.load(dataFile)

	test_maxent(model, data)

else:
	print "Useage: python test.py modelFile dataFile"
	print "    Where modelFile is the name of the saved model file"
	print "      and dataFile is the name of tha saved data file to test with"
