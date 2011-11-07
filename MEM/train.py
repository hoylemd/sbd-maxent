import pickle
import nltk


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
	

def train_maxent(algorithm):
	print "in train_maxent"
	try:
		classifier = nltk.MaxentClassifier.train(train, 'GIS', trace=0, max_iter=1000)
	except Exception, e:
		classifier = e

	f = open("classdemo.model", 'w');

	pickle.dump(classifier, f)
	

train_maxent(nltk.classify.MaxentClassifier.ALGORITHMS[0])
