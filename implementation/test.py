import nltk
import pickle
import sys
import string
import features


def setupData(filename):
	f = open(filename, 'r')

	lines = f.readlines()
	
	contexts = []

	for line in lines:
		words = (string.split(line))
	#	for word in words:
	#		print word + " ",
	#	print
		contexts.append(words)

	contextFeatures = []	
	for context in contexts:
		feats = features.testFeatures(context)
		contextFeatures.append(feats)

	return contextFeatures

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
	data = setupData(sys.argv[1])

	modelFile = open(sys.argv[2], 'r')
	model = pickle.load(modelFile)

	test_maxent(model, data)

else:
	print "Useage: python test.py dataFile modelFile"
	print "    Where <dataFile> is the name of a context file generated by  Contextualizer,"
	print "    and <modelFile> is the name of the saved model file"
