"""
訓練済みモデルのテストをするプログラム。
"""

import os
import sys
import numpy as np
from keras.models import load_model
from modules.funcs import Field1ToField2

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

    output = model.predict(Field1ToField2(input).reshape([1, 6, 6, 3]))
    output = output.reshape(input.shape)
    output = np.round(output, 4)

    print()
    print("Input: ")
    print(input)
    print()

    print("Output: ")
    print(output)
    print()
