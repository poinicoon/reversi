import sys
import numpy as np

import config
from field import Field
from game import Game
# from player import PlayerHuman
# from player import PlayerTrained
# from player import PlayerMax
# from player import PlayerRandomAll
from player import PlayerRandomValidOnly


def play_game(field_size: np.ndarray, fields, coords) -> (int, [np.ndarray], [np.ndarray]):
    field = Field(field_size)
    players = (PlayerRandomValidOnly(0, field_size), PlayerRandomValidOnly(1, field_size))

    game_ins = Game(field, players, fields, coords)
    winner, fields, coords = game_ins.start()

    return winner, fields, coords


if __name__ == "__main__":

    # フィールドサイズ
    field_size = np.array([6, 6])

    x_train = []  # type: [np.ndarray]
    y_train = []  # type: [np.ndarray]

    epoch = 1000

    for i in range(epoch):
        sys.stdout.write("\r" + "make_datasets: " + str(i + 1) + "/" + str(epoch))
        winner, x_train, y_train = play_game(field_size, x_train, y_train)
    print()

    if not config.DIR_CONFIG.exists():
        config.DIR_CONFIG.mkdir()

    np.save(config.PATH_XTRAIN, x_train)
    np.save(config.PATH_YTRAIN, y_train)

    print("Saved Datasets: " + str(len(y_train)))
    print()
