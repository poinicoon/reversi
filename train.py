import numpy as np
from keras.layers import Activation, BatchNormalization, Conv2D, Flatten, InputLayer, MaxPooling2D
from keras.models import Sequential, load_model
from keras.utils import plot_model

from config import PATH_MODEL, PATH_MODELIMAGE, PATH_XTRAIN, PATH_YTRAIN, PATH_XTEST, PATH_YTEST


class Train:
    x_train = None  # type: np.ndarray
    x_test = None  # type: np.ndarray
    y_train = None  # type: np.ndarray
    y_test = None  # type: np.ndarray

    '''
    def make_model(self) -> Sequential:
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

    def make_model(self) -> Sequential:
        model = Sequential()
        model.add(InputLayer(input_shape=(self.x_train.shape[1:])))

        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(1, 1), padding='same'))

        model.add(BatchNormalization())

        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(1, 1), padding='same'))

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

    def load_model(self) -> Sequential:
        return load_model(PATH_MODEL)

    def save_model(self, model) -> None:
        model.save(PATH_MODEL)

    def save_png(self, model) -> None:
        plot_model(model, to_file=str(PATH_MODELIMAGE), show_shapes=True)

    def train(self, model) -> Sequential:
        batch_size = 64
        epochs = 100

        history = model.fit(self.x_train,
                            self.y_train,
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=1)

        score = model.evaluate(self.x_test, self.y_test, verbose=1)

        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

        return model

    def __init__(self):
        self.x_train = np.load(PATH_XTRAIN)
        self.y_train = np.load(PATH_YTRAIN)
        self.x_test = np.load(PATH_XTEST)
        self.y_test = np.load(PATH_YTEST)


if __name__ == "__main__":
    train = Train()
    if PATH_MODEL.exists():
        model = train.load_model()
    else:
        model = train.make_model()
        train.save_png(model)

    model = train.train(model)
    train.save_model(model)
