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
test = [
    (dict(a=1,b=0,c=1)), # unseen
    (dict(a=1,b=0,c=0)), # unseen
    (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
    (dict(a=0,b=1,c=0)), # seen 1 time, label=x
    ]

def test_maxent(algorithms):
    classifiers = {}
    for algorithm in nltk.classify.MaxentClassifier.ALGORITHMS:
        if algorithm.lower() == 'megam':
            try: nltk.classify.megam.config_megam()
            except: raise #continue
        try:
            classifiers[algorithm] = nltk.MaxentClassifier.train(
                    train, algorithm, trace=0, max_iter=1000)
        except Exception, e:
            classifiers[algorithm] = e
    print ' '*11+''.join(['      test[%s]  ' % i
                          for i in range(len(test))])
    print ' '*11+'     p(x)  p(y)'*len(test)
    print '-'*(11+15*len(test))
    for algorithm, classifier in classifiers.items():
        print '%11s' % algorithm,
        if isinstance(classifier, Exception):
            print 'Error: %r' % classifier; continue
        for featureset in test:
            pdist = classifier.prob_classify(featureset)
            print '%8.2f%6.2f' % (pdist.prob('x'), pdist.prob('y')),
        print
test_maxent(nltk.classify.MaxentClassifier.ALGORITHMS)
