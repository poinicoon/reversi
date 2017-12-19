import numpy as np
from itertools import product

from funcs import IsCoordValid
from player_base import PlayerBase


class PlayerRandomValidOnly(PlayerBase):
    def execute_(self, field: np.ndarray) -> np.ndarray:

        put_coord_list = []  # type: [np.ndarray]

        for col, row in product(range(field.shape[0]), range(field.shape[1])):
            tmp_coord = np.array([col, row])
            if IsCoordValid(field, tmp_coord, self.get_player_number()):
                put_coord_list.append(tmp_coord)

        return put_coord_list[np.random.randint(len(put_coord_list))]

    def __init__(self, player_num: int, field_size: np.array, *, player_name="RandomValidOnly") -> None:
        super(PlayerRandomValidOnly, self).__init__(player_num, field_size, player_name=player_name)
