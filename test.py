import numpy as np
import keras

import config

input = np.array([[[[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                   [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]]])

print("Input")
for col in range(input.shape[1]):
    for row in range(input.shape[2]):
        if input[0, col, row, 0] == 1:
            print("-", end=" ")
        elif input[0, col, row, 1] == 1:
            print("1", end=" ")
        elif input[0, col, row, 2] == 1:
            print("2", end=" ")
    print()

print()

model = keras.models.load_model(config.ModelPath)

output = model.predict(input)

output = output.reshape(6, 6)

output = np.round(output, 4)

for col in range(output.shape[0]):
    for row in range(output.shape[1]):
        print(output[col, row], end=" ")
    print()
