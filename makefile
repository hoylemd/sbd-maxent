brownLoc = data/brown.txt
brownLength = 51763

Corpus = ${brownLoc}
CorpusLength = ${brownLength}

Input = ${brownLoc}

trainSize = 5000
remainderSize = 46763
demoSize = 200

modelName = main.model

remainderFile = remainder.sample

trainSample = train.sample
testSample = test.sample
demoSample = demo.sample

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
	./SplitSample ${demoSize} ${remainderSize} ${remainderFile} ${testSample} | ./newlineStripper > ${demoSample}
	rm ${remainderFile}

train : splitData
	cat ${trainSample} | ./Contextualizer > train.context
	python train.py train.context ${modelName}

test : ${modelName} ${testSample}
	cat ${testSample} | ./Contextualizer > test.context
	python test.py test.context ${modelName} > ${results}

demo : ${modelName} ${demoSample}
	cat ${demoSample} | ./Contextualizer > demo.context
	python execute.py demo.context ${modelName} > demo.classification
	cat ${demoSample} | ./Replacer demo.classification > ${output}

execute : ${modelName} ${Input}
	cat ${Input} | ./Contextualizer > execute.context
	python execute.py execute.context ${modelName} > execute.classification
	cat ${Input} | ./Replacer execute.classification > ${output}

clean :
	cd csrc && $(MAKE) clean
	rm -f *.pyc Contextualizer GetSample SplitSample stopwatch Replacer newlineStripper *.model *.context featureTestResults.txt testResults.txt stopwatch.start time.txt con1.txt *.sample *.classification *.disambiguated *.report
