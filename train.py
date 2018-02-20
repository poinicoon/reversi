import os
import sys
import numpy as np
from keras.layers import Activation, BatchNormalization, Conv2D, Flatten, InputLayer, MaxPooling2D
from keras.models import Sequential, load_model

field_size = (6, 6)

'''
def make_model():
    model = Sequential()
    model.add(InputLayer(input_shape=(self.x_train.shape[1:])))
    model.add(Conv2D(64, self.x_train.shape[1:3], padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(1, (1, 1), padding='same', activation='relu', use_bias=True))
    model.add(Flatten())
    model.add(Activation('relu'))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="SGD", metrics=['accuracy'])

    return model
'''


def make_model():
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


def train(model, x_train, y_train, x_test, y_test):
    batch_size = 64
    epochs = 100

    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)

    score = model.evaluate(x_test, y_test, verbose=1)

    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    return model


if __name__ == "__main__":
    model_path = sys.argv[1]
    x_train_path = sys.argv[2]
    y_train_path = sys.argv[3]
    x_test_path = sys.argv[4]
    y_test_path = sys.argv[5]

    if os.path.exists(model_path):
        model = load_model(model_path)
    else:
        model = make_model()

    x_train = np.load(x_train_path)
    y_train = np.load(y_train_path)
    x_test = np.load(x_test_path)
    y_test = np.load(y_test_path)

    model = train(model, x_train, y_train, x_test, y_test)
    model.save(model_path)
