import numpy as np
from itertools import product

from player_base import PlayerBase
from funcs import GetNumOfGettablePosition


class PlayerMax(PlayerBase):
    def execute_(self, field: np.ndarray) -> np.ndarray:

        max_num = 0
        max_pos = None  # type: np.ndarray

        for col, row in product(range(field.shape[0]), range(field.shape[1])):
            tmp_num = GetNumOfGettablePosition(field, np.array([col, row]), self.get_player_number())
            if max_num < tmp_num:
                max_num = tmp_num
                max_pos = np.array([col, row])

        return max_pos

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Max") -> None:
        super(PlayerMax, self).__init__(player_num, field_size, player_name=player_name)
