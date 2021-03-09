#!/bin/bash

counter=100
while [ $counter -le 190 ]
do
   grep "$counter" LexerSuite.py | wc -l
   echo $counter
   ((counter++))
done
