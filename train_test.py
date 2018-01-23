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
    if col == 0:
        print("& 0 & 1 & 2 & 3 & 4 & 5 \\\\ \\hline \\hline")
    print(col, end="")
    print(" & ", end="")
    for row in range(input.shape[2]):
        if 0 < row:
            print(" & ", end="")
        if input[0, col, row, 0] == 1:
            print("-", end="")
        elif input[0, col, row, 1] == 1:
            print("1", end="")
        elif input[0, col, row, 2] == 1:
            print("2", end="")
        print(" ", end="")
    print(" \\\\ \\hline")

print()

model = keras.models.load_model(config.ModelPath)

output = model.predict(input)

output = output.reshape(6, 6)

for col in range(output.shape[0]):
    if col == 0:
        print("& 0 & 1 & 2 & 3 & 4 & 5 \\\\ \\hline \\hline")
    print(col, end="")
    print(" & ", end="")
    for row in range(output.shape[1]):
        if 0 < row:
            print(" & ", end="")
        print(output[col, row], end="")
    print(" \\\\ \\hline")

print()

avg = np.average(output)

print("平均値: ", end="")
print(avg)

print("座標: ", end="")
for col in range(output.shape[0]):
    for row in range(output.shape[1]):
        if output[col, row] > avg:
            print("(" + str(col) + ", " + str(row) + "), ", end="")