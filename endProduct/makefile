brownLength = 51763
trainSize = 250
testSize = 1000
demoSize = 50

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

train : install trainFile.txt
	cat brownTrain.txt | ./Contextualizer > brownTrain.context
	python train.py brownTrain.context brownModel.model

testModel.model : train

test : testFeatures testClassify

execute :
	python execute.py con1.context brownModel.model > con1.classification
	cat con1.sample | ./Replacer con1.classification > con1.disambiguated

con1 : install
	./GetSample ${demoSize} ${brownLength} brown.txt > con1.txt
	cat con1.txt | ./newlineStripper > con1.sample
	cat con1.sample | ./Contextualizer > con1.context

trainBrown : install
	./GetSample ${trainSize} ${brownLength} brown.txt | ./Contextualizer > brownTrain.context
	python train.py brownTrain.context brownModel.model

justforfun : install
	./stopwatch start > stopwatch.start
	./GetSample ${trainSize} ${brownLength} brown.txt | ./Contextualizer > brownTrain.context
	cat brown.txt | ./Contextualizer > brownTest.context
	python train.py brownTrain.context brownModel.model
	python test.py brownTest.context brownModel.model > testResults.txt
	cat stopwatch.start | ./stopwatch stop > time.txt
	rm stopwatch.start
	echo Results:
	echo Elapsed Time:

testClassify : install testFile.txt testModel.model
	cat brownTest.txt | ./Contextualizer > brownTest.context
	python test.py brownTest.context brownModel.model > testResults.txt

testFeatures: FeatureModule testFeatures.py
	python testFeatures.py > featureTestResults.txt

clean :
	rm -f *.pyc Contextualizer GetSample stopwatch Replacer newlineStripper *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt con1.txt *.sample *.classifications
