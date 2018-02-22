# -*- coding: utf-8 -*-

"""
テストデータを作成するためのプログラム。
コマンドラインから実行する。コマンドライン引数として、第1引数にテストデータXのファイル名、第2引数にテストデータYのファイル名を与える。
"""

import sys
import numpy as np
from modules.funcs import GetTestCoord, Softmax
from modules.field import Field
from modules.game import Game
from modules.player import PlayerRandom

field_size = np.array([6, 6])


def play_game():
    '''
    ゲームを開始させる。
    :return: X, Y
    '''
    field = Field(field_size)

    players = (PlayerRandom(0, field_size),
               PlayerRandom(1, field_size))

    game = Game(field, players, stdout=False)
    _, x, y = game.start()

    return x, y


def main(x_test_path, y_test_path):
    epoch = 1000

    x = None

    print("Generating Testdata")

    for i in range(epoch):
        progress = ((i + 1) / (epoch / 100)) / 2
        print("\r{0}%".format(progress), end="")
        _x, _ = play_game()
        if i < 1:
            x = _x
        else:
            x = np.concatenate([x, _x], axis=0)

    y = []

    for i in range(len(x)):
        progress = ((i + 1) / (len(x) / 100)) / 2
        print("\r{0}%".format(progress + 50), end="")
        y.append(Softmax(GetTestCoord(x[i])))

    print()

    np.save(x_test_path, x)
    np.save(y_test_path, y)

    print("Testdata length: " + str(len(y)))
    print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
