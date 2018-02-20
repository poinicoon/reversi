import sys
import numpy as np

import config
from field import Field
from game import Game
# from player import PlayerHuman
# from player import PlayerTrained
# from player import PlayerMax
from player import PlayerRandom


def play_game(field_size: np.ndarray) -> (int, [np.ndarray], [np.ndarray]):
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

    '''
    if not config.WORK_DIR.exists():
        config.WORK_DIR.mkdir()
    np.save(config.X_TRAIN_PATH, x)
    np.save(config.Y_TRAIN_PATH, y)
    '''
    np.save(x_train_path, x)
    np.save(y_train_path, y)

    print("Traindata length: " + str(len(y)))
    print()
