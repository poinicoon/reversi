import numpy as np

from player_base import PlayerBase

from funcs import GetNumOfGettablePosition


class PlayerMax(PlayerBase):
    def execute_(self, field: np.ndarray) -> np.ndarray:

        max_num = 0
        max_pos = np.zeros([2])

        for col in range(field.shape[0]):
            for row in range(field.shape[1]):
                tmp_num = GetNumOfGettablePosition(field, np.array([col, row]), self.get_player_number())
                if max_num < tmp_num:
                    max_num = tmp_num
                    max_pos = np.array([col, row])

        return max_pos

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Max"):
        super(PlayerMax, self).__init__(player_num, field_size, player_name=player_name)
