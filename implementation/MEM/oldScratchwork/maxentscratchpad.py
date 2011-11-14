import nltk

print "hi!"

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
	
test = [
    (dict(a=1,b=0,c=1)), # unseen
    (dict(a=1,b=0,c=0)), # unseen
    (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
    (dict(a=0,b=1,c=0)), # seen 1 time, label=x
    ]

def test_maxent(algorithm):
	print "in test_maxent"
	try:
		classifier = nltk.MaxentClassifier.train(train, 'GIS', trace=0, max_iter=1000)
	except Exception, e:
		classifier = e
	
	if isinstance(classifier, Exception):
		print 'Error: %r' % classifier
	else:
		i = 1;
		for featureset in test:
			print "Test #%d:" % (i),
			i += 1
			pdist = classifier.prob_classify(featureset)
			label = classifier.classify(featureset)
			print 'x: %.2f y: %.2f descision: %s' % (pdist.prob('x'), pdist.prob('y'), label)

print "starting"		
nltk.classify.MaxentClassifier.ALGORITHMS
test_maxent(nltk.classify.MaxentClassifier.ALGORITHMS[0])
