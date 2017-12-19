import os
import sys
import json
import numpy as np

from field import Field
from game import Game
from player_base import PlayerBase
from player_random_all import PlayerRandomAll
from player_random_valid_only import PlayerRandomValidOnly

config = json.load(open("config.json", "r"))


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
if not os.path.isdir(config["work_dir"]):
    os.mkdir(config["work_dir"])

np.save(config["x_train_path"], fields)
np.save(config["y_train_path"], coords)

print("Saved Datasets: " + str(len(coords)))
print()
