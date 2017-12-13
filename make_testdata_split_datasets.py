import os
import json
import numpy as np
from sklearn.model_selection import train_test_split

from funcs import GetCoordNum, GetTestCoord

config = json.load(open("config.json", "r"))

# データセット読み込み
x_train = np.load(config["x_train_path"])
y_train = np.load(config["y_train_path"])

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.33, random_state=111)

np.save(config["x_train_path"], x_train)
np.save(config["y_train_path"], y_train)
np.save(config["x_test_path"], x_test)
np.save(config["y_test_path"], y_test)
