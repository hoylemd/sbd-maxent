brownLength = 51763
trainSize = 250
testSize = 1000

all : install

install : CTools TrainScript TestScript

CTools : 
	cd csrc && $(MAKE)
	cp csrc/Contextualizer .
	cp csrc/GetSample .
	cp csrc/stopwatch .	

TrainScript: train.py FeatureModule

TestScript: test.py FeatureModule

FeatureModule: features.py

train : install trainFile.txt
	cat brownTrain.txt | ./Contextualizer > brownTrain.context
	python train.py brownTrain.context brownModel.model

testModel.model : train

test : testFeatures testClassify

execute : install
	./stopwatch start > stopwatch.start
	./GetSample ${trainSize} ${brownLength} brown.txt | ./Contextualizer > brownTrain.context
	./GetSample ${testSize} ${brownLength} brown.txt | ./Contextualizer > brownTest.context
	python train.py brownTrain.context brownModel.model
	python test.py brownTest.context brownModel.model > testResults.txt
	cat stopwatch.start | ./stopwatch stop > time.txt
	rm stopwatch.start
	echo Results:
	cat testResults.txt
	echo Elapsed Time:
	cat time.txt

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
	rm -f *.pyc Contextualizer getSample stopwatch *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt
