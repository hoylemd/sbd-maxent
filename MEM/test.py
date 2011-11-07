import nltk
import pickle
import sys

def test_maxent(model, data):
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
	dataFile = open(sys.argv[1], 'r')
	data = pickle.load(dataFile)

	modelFile = open(sys.argv[2], 'r')
	model = pickle.load(modelFile)

	test_maxent(model, data)

else:
	print "Useage: python test.py dataFile modelFile"
	print "    Where dataFile is the name of the saved data file to test with"
	print "      and modelFileFile is the name of the saved model file"
