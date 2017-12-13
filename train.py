import os
import json
import numpy as np
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Activation, BatchNormalization, Conv2D, Dense, Dropout, Flatten, InputLayer, MaxPooling2D
from keras.models import Sequential, model_from_json
from keras.optimizers import Adam, RMSprop, SGD
from keras.losses import categorical_crossentropy, mean_squared_error
from keras.utils import to_categorical, plot_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

config = json.load(open("config.json", "r"))


class Train:
    x_train = None  # type: np.ndarray
    x_test = None  # type: np.ndarray
    y_train = None  # type: np.ndarray
    y_test = None  # type: np.ndarray

    model = None

    def plot(self, epochs, history):
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        plt.plot(range(epochs), loss, marker='.', label='loss')
        plt.plot(range(20), val_loss, marker='.', label='val_loss')
        plt.legend(loc='best', fontsize=10)
        plt.grid()
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.show()

        acc = history.history['acc']
        val_acc = history.history['val_acc']

        # accuracyのグラフ
        plt.plot(range(20), acc, marker='.', label='acc')
        plt.plot(range(20), val_acc, marker='.', label='val_acc')
        plt.legend(loc='best', fontsize=10)
        plt.grid()
        plt.xlabel('epoch')
        plt.ylabel('acc')
        plt.show()

    def make_model(self):
        model = Sequential()
        model.add(InputLayer(input_shape=(8, 8, 3)))
        model.add(Conv2D(3, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(32, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(16, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(1, (3, 3), padding='same'))
        model.add(Activation('relu'))

        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Flatten())

        self.model = model

    def load_model(self):
        self.model = model_from_json(open(config["model_path"], 'r').read())

        self.model.load_weights(config["weights_path"])

    def save_model(self):
        open(config["model_path"], "w").write(self.model.to_json())

        self.model.save_weights(config["weights_path"])

    def save_png(self):
        plot_model(self.model, to_file=config["model_image_path"], show_shapes=True)

    def train(self):
        model = self.model

        batch_size = 128
        epochs = 30

        model.compile(loss='mean_squared_error', optimizer="adam", metrics=['accuracy'])

        history = model.fit(self.x_train, self.y_train, batch_size=batch_size, epochs=epochs, verbose=0)

        score = model.evaluate(self.x_test, self.y_test, verbose=1)

        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

    def __init__(self, field_size: np.ndarray):
        # フィールドの要素数
        num_classes = field_size[0] * field_size[1]

        # データセット読み込み
        #X = np.load(config["x_train_path"])
        #Y = np.load(config["y_train_path"])

        # 学習データとテストデータに分ける
        #self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=0.33, random_state=111)

        self.x_train = np.load(config["x_train_path"])
        self.y_train = np.load(config["y_train_path"])
        self.x_test = np.load(config["x_test_path"])
        self.y_test = np.load(config["y_test_path"])


field_size = np.array([8, 8])

train = Train(field_size)
if os.path.exists(config["model_path"]):
    train.load_model()
else:
    train.make_model()
    train.save_png()
train.train()
train.save_model()
