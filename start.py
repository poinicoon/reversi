import os
import json
import numpy as np

from field import Field
from game import Game
from player_base import PlayerBase
from player_random_all import PlayerRandomAll

config = json.load(open("config.json", "r"))


def play_game(field_size: np.ndarray) -> (int, [np.ndarray], [np.ndarray]):
    field_ins = Field(field_size)  # type: Field
    players_ins = (PlayerRandomAll(0, field_size), PlayerRandomAll(1, field_size))  # type: (PlayerBase, PlayerBase)

    game_ins = Game(field_ins, players_ins, [], [])  # type: Game
    winner, fields, coords = game_ins.start()

    return winner, fields, coords


# フィールドサイズ
field_size = np.array([8, 8])  # type: np.ndarray

winner, fields, coords = play_game(field_size)

print("Winner: Player" + str(winner))
print()
