#!/bin/bash -eu

epoch=1000

for ((i=0 ; i<epoch ; i++))
do
	echo -n "loop: "
	echo $epoch

	~/venv/bin/python3 make_datasets.py
	~/venv/bin/python3 make_testdata_from_datasets.py
	~/venv/bin/python3 train.py

done
