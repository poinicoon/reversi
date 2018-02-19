import os
import numpy as np
import keras

from config import PATH_MODEL
from funcs import GetField3dimOnehot

if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    input = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 2, 0, 0],
                      [0, 0, 2, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]])

    model = keras.models.load_model(PATH_MODEL)

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
