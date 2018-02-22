# -*- coding: utf-8 -*-

"""
訓練データを作成するためのプログラム。
コマンドラインから実行する。コマンドライン引数として、第1引数に訓練データXのファイル名、第2引数に訓練データYのファイル名を与える。
"""

import sys
import numpy as np
from modules.field import Field
from modules.game import Game
# from player import PlayerHuman
# from player import PlayerTrained
# from player import PlayerMax
from modules.player import PlayerRandom

field_size = (6, 6)


def play_game(field_size):
    field = Field(field_size)
    players = (PlayerRandom(0, field_size), PlayerRandom(1, field_size))

    game = Game(field, players)
    _, x, y = game.start()

    return x, y


def main(x_train_path, y_train_path):
    epoch = 10

    x = None
    y = None

    print("Generating Traindata")
    for i in range(epoch):
        progress = (i + 1) / (epoch / 100)
        print("\r{0}%".format(progress), end="")
        _x, _y = play_game(field_size)
        if i < 1:
            x = _x
            y = _y
        else:
            x = np.concatenate([x, _x], axis=0)
            y = np.concatenate([y, _y], axis=0)
    print()

    np.save(x_train_path, x)
    np.save(y_train_path, y)

    print("Traindata length: " + str(len(y)))
    print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
