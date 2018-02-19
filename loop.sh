#!/bin/bash -eu

python3 make_traindata.py
python3 make_testdata.py

while true
do
  python3 make_traindata.py
  python3 train.py
done
