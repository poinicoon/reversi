import os
import json
import numpy as np

from funcs import get_test_coord

config = json.load(open("config.json", "r"))

# データセット読み込み
x_train = np.load(config["x_train_path"])
y_train = np.load(config["y_train_path"])

y_test = []

for i in range(len(y_train)):
    y_test.append(get_test_coord(y_train[1]))

np.save(config["x_test_path"], x_train)
np.save(config["y_test_path"], y_test)