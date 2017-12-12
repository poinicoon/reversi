import os
import numpy as np
from keras.callbacks import EarlyStopping
from keras.layers import Activation, BatchNormalization, Conv2D, Dense, Dropout, Flatten, InputLayer, MaxPooling2D
from keras.models import Sequential, model_from_json
from keras.optimizers import Adam, RMSprop, SGD
from keras.losses import categorical_crossentropy, mean_squared_error
from keras.utils import to_categorical, plot_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

work_dir = os.environ["HOME"] + os.sep + "reversi_learn"


class Train:
    X_train = None  # type: np.ndarray
    X_test = None  # type: np.ndarray
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
        model.add(InputLayer(input_shape=(3, 8, 8)))
        model.add(Conv2D(64, (3, 3), padding='same', data_format='channels_first'))
        model.add(Conv2D(32, (3, 3), padding='same', data_format='channels_first'))
        model.add(Conv2D(1, (3, 3), padding='same', data_format='channels_first'))
        # softmax
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Activation('softmax'))
        model.add(Flatten())
        # (3, 8, 8)

        self.model = model

    def load_model(self):
        self.model = model_from_json(open(work_dir + "model.json", 'r').read())

        self.model.load_weights(work_dir + os.sep + "weights.h5")

    def save_model(self):
        open(work_dir + "model.json", "w").write(self.model.to_json())

        self.model.save_weights(work_dir + os.sep + "weights.h5")

    def save_png(self):
        plot_model(self.model, to_file=work_dir + os.sep + "model.png", show_shapes=True)

    def train(self):
        model = self.model

        batch_size = 128
        epochs = 20

        model.compile(loss='categorical_crossentropy',
                      optimizer=SGD(),
                      metrics=['accuracy'])

        history = model.fit(self.X_train,
                            self.y_train,
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=1,
                            validation_split=0.1)

        score = model.evaluate(self.X_test, self.y_test, verbose=1)

        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

    def __init__(self, field_size: np.ndarray):
        # フィールドの要素数
        num_classes = field_size[0] * field_size[1]

        # データセット読み込み
        X = np.load(work_dir + os.sep + "datasets_x.npy")
        Y = np.load(work_dir + os.sep + "datasets_y.npy")

        # one-hot
        Y = to_categorical(Y, num_classes)

        # 学習データとテストデータに分ける
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y,
                                                                                test_size=0.33,
                                                                                random_state=111)


field_size = np.array([8, 8])

train = Train(field_size)
# train.load_model()
train.make_model()
train.save_png()
train.train()
train.save_model()
