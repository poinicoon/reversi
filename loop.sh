#!/bin/bash -eu

epoch=1000

python3 make_datasets.py > /dev/null
# python3 make_testdata_from_datasets.py > dev/null
python3 make_testdata_split_datasets.py > dev/null

for ((i=0 ; i<$epoch ; i++))
do
	echo "loop: "$((i+1))"/"$epoch

	python3 make_datasets.py
	python3 train.py

done
