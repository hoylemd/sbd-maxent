brownLoc = data/brown.txt
brownLength = 51763
reutersLoc = data/reuters.txt
reutersLength = 386830
remainderFile = test.sample

targetCorpus = ${reutersLoc}

trainingCorpus = ${brownLoc}
trainingLength = ${brownLength}

testCorpus = ${brownLoc}
testLength = ${reutersLength}

trainSize = 5000
testSize = 46763
demoSize = 50000


modelName = main.model

all : install

install : CTools TrainScript TestScript

CTools :
	cd csrc && $(MAKE)
	cp csrc/Contextualizer .
	cp csrc/GetSample .
	cp csrc/SplitSample .
	cp csrc/stopwatch .
	cp csrc/Replacer .
	cp csrc/newlineStripper .

TrainScript: train.py FeatureModule

TestScript: test.py FeatureModule

FeatureModule: features.py

testModel : install ${trainingCorpus}
	./SplitSample ${trainSize} ${trainingLength} ${trainingCorpus} ${remainderFile}| ./Contextualizer > train.context
	python train.py train.context ${modelName}

testClassify : install testModel
	cat ${remainderFile} | ./Contextualizer > test.context
	python test.py test.context ${modelName} > testResults.report

testFeatures: FeatureModule testFeatures.py
	python testFeatures.py > featureTestResults.txt

test : testFeatures testClassify

model : install ${trainingCorpus}
	./GetSample ${trainSize} ${trainingLength} ${trainingCorpus} | ./Contextualizer -> train.context
	python train.py train.context ${modelName}

con1 : install ${targetCorpus}
	cat ${targetCorpus} | ./newlineStripper > con1.sample
	cat con1.sample | ./Contextualizer > con1.context

execute : model con1
	python execute.py con1.context ${modelName} > con1.classification
	./GetSample ${testSize} ${testLength} ${targetCorpus}|./Replacer con1.classification > con1.disambiguated

clean :
	cd csrc && $(MAKE) clean
	rm -f *.pyc Contextualizer GetSample SplitSample stopwatch Replacer newlineStripper *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt con1.txt *.sample *.classification *.disambiguated *.report
