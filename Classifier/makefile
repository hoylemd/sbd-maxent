brownLoc = data/brown.txt
brownLength = 51763
reutersLoc = data/reuters.txt

targetCorpus = ${brownLoc}

trainingCorpus = ${brownLoc}
trainingLength = ${brownLength}

testCorpus = ${brownLoc}
testLength = ${brownLength}

trainSize = 500
testSize = 1000
demoSize = 50

modelName = main.model

all : install

install : CTools TrainScript TestScript

CTools :
	cd csrc && $(MAKE)
	cp csrc/Contextualizer .
	cp csrc/GetSample .
	cp csrc/stopwatch .
	cp csrc/Replacer .
	cp csrc/newlineStripper .

TrainScript: train.py FeatureModule

TestScript: test.py FeatureModule

FeatureModule: features.py

testModel : install ${trainingCorpus}
	./GetSample ${trainSize} ${trainingLength} ${trainingCorpus} | ./Contextualizer > train.context
	python train.py train.context ${modelName}

testClassify : install testModel ${testCorpus}
	./GetSample ${testSize} ${testLength} ${testCorpus} | ./Contextualizer > test.context
	python test.py test.context ${modelName} > testResults.report

testFeatures: FeatureModule testFeatures.py
	python testFeatures.py > featureTestResults.txt

test : testFeatures testClassify

model : install ${trainingCorpus}
	cat ${trainingCorpus} | ./Contextualizer -> train.context
	python train.py train.context ${modelName}

con1 : install ${targetCorpus}
	cat ${targetCorpus} | ./newlineStripper > con1.sample
	cat con1.sample | ./Contextualizer > con1.context

execute : model con1
	python execute.py con1.context ${modelName} > con1.classification
	cat con1.sample | ./Replacer con1.classification > con1.disambiguated

clean :
	cd csrc && $(MAKE) clean
	rm -f *.pyc Contextualizer GetSample stopwatch Replacer newlineStripper *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt con1.txt *.sample *.classification *.disambiguated *.report
