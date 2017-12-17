import numpy as np

from player_base import PlayerBase


class PlayerMax(PlayerBase):
    def execute_(self, raw_field: np.ndarray) -> np.ndarray:
        print(raw_field + 1)

        print("Input col: ", end="")
        col = int(input())  # type: int
        print("Input row: ", end="")
        row = int(input())  # type: int
        return np.array([col, row])

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Max"):
        super(PlayerMax, self).__init__(player_num, field_size, player_name=player_name)
