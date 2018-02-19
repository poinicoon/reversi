import sys
import numpy as np

from config import PATH_XTRAIN, PATH_YTRAIN, PATH_XTEST, PATH_YTEST
from funcs import GetTestCoord, Softmax

# データセット読み込み
x_train = np.load(PATH_XTRAIN)
y_train = np.load(PATH_YTRAIN)

y_test = []

for i in range(len(x_train)):
    sys.stdout.write("\r" + "make_testdata: " + str(i + 1) + "/" + str(len(x_train)))
    y_test.append(Softmax(GetTestCoord(x_train[i])))

print()

np.save(PATH_XTEST, x_train)
np.save(PATH_YTEST, y_test)
