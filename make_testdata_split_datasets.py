import os
import json
import numpy as np
from sklearn.model_selection import train_test_split

from config import XTrainPath, YTrainPath, XTestPath, YTestPath

# データセット読み込み
x_train = np.load(XTrainPath)
y_train = np.load(YTrainPath)

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.33, random_state=111)

np.save(XTrainPath, x_train)
np.save(YTrainPath, y_train)
np.save(XTestPath, x_test)
np.save(YTestPath, y_test)
