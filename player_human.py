import numpy as np

from player_base import PlayerBase


class PlayerHuman(PlayerBase):
    def execute_(self, field: np.ndarray) -> np.ndarray:
        print("col >>> ", end="")
        col = int(input())
        print("row >>> ", end="")
        row = int(input())
        return np.array([col, row])

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Human") -> None:
        super(PlayerHuman, self).__init__(player_num, field_size, player_name=player_name)
