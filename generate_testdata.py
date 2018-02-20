import sys
import numpy as np
from funcs import GetTestCoord, Softmax
from field import Field
from game import Game
from player import PlayerRandom


def play_game(field_size: np.ndarray) -> (int, [np.ndarray], [np.ndarray]):
    field = Field(field_size)
    players = (PlayerRandom(0, field_size), PlayerRandom(1, field_size))

    game = Game(field, players)
    _, x, y = game.start()

    return x, y


if __name__ == "__main__":

    x_test_path = sys.argv[1]
    y_test_path = sys.argv[2]

    field_size = np.array([6, 6])

    epoch = 10

    x = None

    print("Generating Testdata")

    for i in range(epoch):
        progress = ((i + 1) / (epoch / 100)) / 2
        print("\r{0}%".format(progress), end="")
        _x, _ = play_game(field_size)
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
    '''
    if not WORK_DIR.exists():
        WORK_DIR.mkdir()
    np.save(X_TEST_PATH, x)
    np.save(Y_TEST_PATH, y)
    '''
    np.save(x_test_path, x)
    np.save(y_test_path, y)

    print("Testdata length: " + str(len(y)))
    print()
