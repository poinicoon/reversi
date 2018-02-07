import numpy as np
from keras.layers import Activation, Conv2D, Flatten, InputLayer
from keras.models import Sequential, load_model
from keras.utils import plot_model

from config import ModelPath, ModelImagePath, XTrainPath, YTrainPath, XTestPath, YTestPath


class Train:
    x_train = None  # type: np.ndarray
    x_test = None  # type: np.ndarray
    y_train = None  # type: np.ndarray
    y_test = None  # type: np.ndarray

    model = None  # type: Sequential

    def make_model(self):
        print(self.x_train.shape[1:3])
        model = Sequential()
        model.add(InputLayer(input_shape=(self.x_train.shape[1:])))
        model.add(Conv2D(64, (6, 6), padding='same', activation='relu'))
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(Conv2D(1, (1, 1), padding='same', activation='relu', use_bias=True))
        model.add(Flatten())
        model.add(Activation('relu'))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy', optimizer="SGD", metrics=['accuracy'])

        self.model = model

    def load_model(self):
        self.model = load_model(ModelPath)

    def save_model(self):
        self.model.save(ModelPath)

    def save_png(self):
        plot_model(self.model, to_file=str(ModelImagePath), show_shapes=True)

    def train(self):
        model = self.model

        batch_size = 64
        epochs = 100
        callbacks = []

        history = model.fit(self.x_train,
                            self.y_train,
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=1,
                            callbacks=callbacks)

        score = model.evaluate(self.x_test, self.y_test, verbose=1)

        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

        self.model = model

    def __init__(self):
        self.x_train = np.load(XTrainPath)
        self.y_train = np.load(YTrainPath)
        self.x_test = np.load(XTestPath)
        self.y_test = np.load(YTestPath)

if __name__ == "__main__":
    train = Train()
    if ModelPath.exists():
        print("load model")
        train.load_model()
    else:
        print("make model")
        train.make_model()
        train.save_png()
    train.train()
    train.save_model()
