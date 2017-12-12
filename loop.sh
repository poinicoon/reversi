#!/bin/bash -eu

epoch=1000

for ((i=0 ; i<epoch ; i++))
do
	echo -n "loop: "
	echo $epoch
	~/venv_reversi_learn/bin/python3 start.py
	~/venv_reversi_learn/bin/python3 train.py
done
