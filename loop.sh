#!/bin/bash -eu

X_TRAIN_PATH="$HOME/.reversi_nn/x_train.npy"
Y_TRAIN_PATH="$HOME/.reversi_nn/y_train.npy"
X_TEST_PATH="$HOME/.reversi_nn/x_test.npy"
Y_TEST_PATH="$HOME/.reversi_nn/y_test.npy"
MODEL_PATH="$HOME/.reversi_nn/model.h5"

python3 generate_testdata.py $X_TEST_PATH $Y_TEST_PATH

while true
do
  python3 generate_traindata.py $X_TRAIN_PATH $Y_TRAIN_PATH
  python3 train.py $MODEL_PATH $X_TRAIN_PATH $Y_TRAIN_PATH $X_TEST_PATH $Y_TEST_PATH
done
