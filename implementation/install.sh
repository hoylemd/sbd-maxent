#! /bin/bash

cd csrc;
make Contextualizer
mv Contextualizer ..
cd .. 
cp dataMaker/dataMaker.py .
cp dataMaker/trainMaker.py .
