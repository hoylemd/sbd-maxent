all : test

test : trainingData.train testingData.test train.py test.py
	python train.py trainingData.train demoModel.model
	python test.py testingData.test demoModel.model

trainingData.train : generateTrainData.py
	python generateTrainData.py trainingData.train

testingData.test : generateTestData.py
	python generateTestData.py testingData.test
