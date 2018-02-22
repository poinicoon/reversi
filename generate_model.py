# -*- coding: utf-8 -*-

"""
モデルを作成する。
"""

import sys
from keras.models import Sequential, InputLayer
from keras.layers import Conv2D, Activation, BatchNormalization, MaxPooling2D, Flatten

field_size = (6, 6)


def make_model():
    """
    model = Sequential()
    model.add(InputLayer(input_shape=(self.x_train.shape[1:])))
    model.add(Conv2D(64, self.x_train.shape[1:3], padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(1, (1, 1), padding='same', activation='relu', use_bias=True))
    model.add(Flatten())
    model.add(Activation('relu'))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="SGD", metrics=['accuracy'])
    """

    model = Sequential()
    model.add(InputLayer(input_shape=(field_size[0], field_size[1], 3)))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    model.add(BatchNormalization())

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    model.add(BatchNormalization())

    model.add(Conv2D(1, (1, 1), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1, 1), padding='same'))

    model.add(BatchNormalization())

    model.add(Flatten())

    model.add(Activation('relu'))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="SGD", metrics=['accuracy'])

    return model


if __name__ == "__main__":
    model_path = sys.argv[1]
    make_model().save(model_path)
