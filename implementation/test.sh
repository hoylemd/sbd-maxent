#! /bin/bash

cat testFile.txt | ./Contextualizer > testFile.context;
cat trainFile.txt | ./Contextualizer > trainFile.context;
python train.py trainFile.context testModel.model;
python test.py testFile.context testModel.model;

