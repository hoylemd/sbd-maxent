from utilities import *

if len(sys.argv) == 3:
    data = setupData(sys.argv[1])
    modelFile = open(sys.argv[2], 'r')
    model = pickle.load(modelFile)
    classifications = execute(model, data)
    for classification in classifications:
        print classification
else:
    print "usage:"
    print " python execute.py <contexts file> <model file>"