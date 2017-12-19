import sys
import numpy as np

import config
from field import Field
from game import Game
from player_base import PlayerBase
from player_random_all import PlayerRandomAll
from player_random_valid_only import PlayerRandomValidOnly


def play_game(field_size: np.ndarray, fields, coords) -> (int, [np.ndarray], [np.ndarray]):
    field_ins = Field(field_size)
    players_ins = (PlayerRandomValidOnly(0, field_size), PlayerRandomValidOnly(1, field_size))

    game_ins = Game(field_ins, players_ins, fields, coords)
    winner, fields, coords = game_ins.start()

    return winner, fields, coords


# フィールドサイズ
field_size = np.array([6, 6])

fields = []  # type: [np.ndarray]
coords = []  # type: [np.ndarray]

epoch = 1000

for i in range(epoch):
    sys.stdout.write("\r" + "make_datasets: " + str(i + 1) + "/" + str(epoch))
    winner, fields, coords = play_game(field_size, fields, coords)
print()

if not config.WorkDir.exists():
    config.WorkDir.mkdir()

np.save(config.XTrainPath, fields)
np.save(config.YTrainPath, coords)



print("Saved Datasets: " + str(len(coords)))
print()
