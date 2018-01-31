import os
import numpy as np
import keras

import config
from funcs import GetField3dimOnehot

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

input = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 2, 0, 0],
                  [0, 0, 2, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]], dtype=int)

model = keras.models.load_model(config.ModelPath)

output = model.predict(GetField3dimOnehot(input - 1).reshape([1, 6, 6, 3]))
output = output.reshape(input.shape)
output = np.round(output, 4)

print()
print("Input: ")
print(input)
print()

print("Output: ")
print(output)
print()
