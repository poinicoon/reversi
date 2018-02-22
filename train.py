#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
訓練
"""

import sys
import numpy as np
import keras

field_size = (6, 6)


def train(model, x_train, y_train, x_test, y_test):
    batch_size = 64
    epochs = 100

    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)

    score = model.evaluate(x_test, y_test, verbose=1)

    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    return model


def main(model_path, x_train_path, y_train_path, x_test_path, y_test_path):
    model = keras.models.load_model(model_path)
    x_train = np.load(x_train_path)
    y_train = np.load(y_train_path)
    x_test = np.load(x_test_path)
    y_test = np.load(y_test_path)

    model = train(model, x_train, y_train, x_test, y_test)
    model.save(model_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
