import os
import sys
import numpy as np
from keras.models import load_model
from funcs import GetField3dimOnehot

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == "__main__":
    model_path = sys.argv[1]
    model = load_model(model_path)

    input = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 2, 0, 0],
                      [0, 0, 2, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]])

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
