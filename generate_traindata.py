import sys
import numpy as np
from field import Field
from game import Game
# from player import PlayerHuman
# from player import PlayerTrained
# from player import PlayerMax
from player import PlayerRandom

field_size = (6, 6)


def play_game(field_size):
    field = Field(field_size)
    players = (PlayerRandom(0, field_size), PlayerRandom(1, field_size))

    game = Game(field, players)
    _, x, y = game.start()

    return x, y


if __name__ == "__main__":

    x_train_path = sys.argv[1]
    y_train_path = sys.argv[2]

    # フィールドサイズ
    field_size = np.array([6, 6])

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
