import pickle
import nltk
import sys

print len(sys.argv)
print sys.argv

def train_maxent(algorithm, trainingData):
	print "in train_maxent"
	try:
		classifier = nltk.MaxentClassifier.train(train, 'GIS', trace=0, max_iter=1000)
	except Exception, e:
		classifier = e	

if len(sys.argv) == 3:
	trainCases = open(sys.argv[1], 'r')
	trainingData = pickle.load(trainCases)

	model = train_maxent(nltk.classify.MaxentClassifier.ALGORITHMS[0], trainingData)
	
	outputModel = open(sys.argv[2], 'w')
	pickle.dump(model, outputModel)

else:
	print "Usage: python train.py <trainCases>.train <nameOfModel>.model"
