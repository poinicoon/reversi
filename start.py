import os
import numpy as np

import field
import game
import player_base
import player_random

work_dir = os.environ["HOME"] + os.sep + "reversi_learn"


def play_game(field_size: np.ndarray, fields, coords) -> (int, [np.ndarray], [np.ndarray]):
    field_ins = field.Field(field_size)  # type: field.Field
    players_ins = (player_random.PlayerRandom(0, field_size),
                   player_random.PlayerRandom(1, field_size))  # type: (player_base.PlayerBase, player_base.PlayerBase)

    game_ins = game.Game(field_ins, players_ins, fields, coords)  # type: game.Game
    winner, fields, coords = game_ins.start()

    return winner, fields, coords


# フィールドサイズ
field_size = np.array([8, 8])  # type: np.ndarray

fields = []  # type: [np.ndarray]
coords = []  # type: [np.ndarray]

epoch = 5  # type: int

for i in range(epoch):
    winner, fields, coords = play_game(field_size, fields, coords)

if not os.path.isdir(work_dir):
    os.mkdir(work_dir)

np.save(work_dir + os.sep + "datasets_x.npy", fields)
np.save(work_dir + os.sep + "datasets_y.npy", coords)

print("Saved Datasets(len: " + str(len(coords)) + ")")
print()