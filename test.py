import os
import numpy as np
import keras

import config

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

input = np.array([[[[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]]])

print("Input: ")
for col in range(input.shape[1]):
    if col == 0:
        print(" ",end=" | ")
        for row in range(input.shape[2]):
            print(row, end=" ")
        print()
        print("-", end="-|-")
        for row in range(input.shape[2]):
            print("-", end="-")
        print()
    print(col, end=" | ")
    for row in range(input.shape[2]):
        if input[0, col, row, 0] == 1:
            print("*", end=" ")
        elif input[0, col, row, 1] == 1:
            print("1", end=" ")
        elif input[0, col, row, 2] == 1:
            print("2", end=" ")
    print()

print()

input2 = np.zeros(input.shape[1:3])
for col in range(input2.shape[0]):
    for row in range(input2.shape[1]):
        if input[0, col, row, 0] == 1:
            continue
        elif input[0, col, row, 1] == 1:
            input2[col, row] = 1
        elif input[0, col, row, 2] == 1:
            input2[col, row] = 2

print(input2)

model = keras.models.load_model(config.ModelPath)

output = model.predict(input)
output = output.reshape(input.shape[1:3])
output = np.round(output, 4)

print("Output: ")
print(output)
