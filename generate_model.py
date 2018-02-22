#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
モデルを作成する。
"""

import sys
from keras.models import Sequential, InputLayer
from keras.layers import Conv2D, Activation, Flatten

field_size = (6, 6)


def make_model():
    model = Sequential()
    model.add(InputLayer(input_shape=field_size))
    model.add(Conv2D(64, (6, 6), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(1, (1, 1), padding='same', activation='relu', use_bias=True))
    model.add(Flatten())
    model.add(Activation('relu'))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="SGD", metrics=['accuracy'])

    return model

def main(model_path):
    model = make_model()
    model.save(model_path)

if __name__ == "__main__":
    main(sys.argv[1])
