#!/bin/bash -eu

epoch=1000

printf "loop"

for ((i=0 ; i<epoch ; i++))
do
	printf "\r"$i"/"$epoch

	~/venv/bin/python3 make_datasets.py
	#~/venv/bin/python3 make_testdata_from_datasets.py
	~/venv/bin/python3 make_testdata_split_datasets.py
	~/venv/bin/python3 train.py

done
