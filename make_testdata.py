import sys
import numpy as np

from config import XTrainPath, YTrainPath, XTestPath, YTestPath
from funcs import GetTestCoord, Softmax

# データセット読み込み
x_train = np.load(XTrainPath)
y_train = np.load(YTrainPath)

y_test = []

for i in range(len(x_train)):
    sys.stdout.write("\r" + "make_testdata: " + str(i + 1) + "/" + str(len(x_train)))
    y_test.append(Softmax(GetTestCoord(x_train[i])))

print()

np.save(XTestPath, x_train)
np.save(YTestPath, y_test)
