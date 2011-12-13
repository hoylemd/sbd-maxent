brownLoc = data/brown.txt
brownLength = 51763

Corpus = ${brownLoc}
CorpusLength = ${brownLength}

trainSize = 5000
remainderSize = 46763
executeSize = 200

modelName = main.model

remainderFile = remainder.sample

trainSample = train.sample
testSample = test.sample
executeSample = execute.sample

results = testResults.report
output = text.disambiguated

all : install

CTools :
	cd csrc && $(MAKE)
	cp csrc/Contextualizer .
	cp csrc/GetSample .
	cp csrc/SplitSample .
	cp csrc/stopwatch .
	cp csrc/Replacer .
	cp csrc/newlineStripper .

FeaturesModule: features.py

UtilitiesModule: utilities.py FeaturesModule

TrainScript: train.py UtilitiesModule

TestScript: test.py UtilitiesModule

ExecuteScript: execute.py UtilitiesModule

install : CTools TrainScript TestScript ExecuteScript

splitData : ${Corpus}
	./SplitSample ${trainSize} ${CorpusLength} ${Corpus} ${remainderFile} > ${trainSample}
	./SplitSample ${executeSize} ${remainderSize} ${remainderFile} ${testSample} | ./newlineStripper > ${executeSample}
	rm ${remainderFile}

train : splitData
	cat ${trainSample} | ./Contextualizer > train.context
	python train.py train.context ${modelName}

test : ${modelName} ${testSample}
	cat ${testSample} | ./Contextualizer > test.context
	python test.py test.context ${modelName} > ${results}

execute : ${modelName} ${executeSample}
	cat ${executeSample} | ./Contextualizer > execute.context
	python execute.py execute.context ${modelName} > execute.classification
	cat ${executeSample} | ./Replacer execute.classification > ${output}

clean :
	cd csrc && $(MAKE) clean
	rm -f *.pyc Contextualizer GetSample SplitSample stopwatch Replacer newlineStripper *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt con1.txt *.sample *.classification *.disambiguated *.report
