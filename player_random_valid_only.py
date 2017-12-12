import numpy as np
import typing

import funcs
import player_base


class PlayerRandomValidOnly(player_base.PlayerBase):
    def execute_(self, raw_field: np.ndarray) -> np.ndarray:

        put_coord_list = []  # type: typing.List[np.ndarray]

        for col in range(raw_field.shape[0]):
            for row in range(raw_field.shape[1]):
                tmp_coord = np.array([col, row])  # type: np.ndarray
                if funcs.is_coord_valid(raw_field, tmp_coord, self.get_player_number()):
                    put_coord_list.append(tmp_coord)

        return put_coord_list[np.random.randint(len(put_coord_list))]

    def __init__(self, player_num: int, field_size: np.array, *, player_name="RandomValidOnly"):
        super(PlayerRandomValidOnly, self).__init__(player_num, field_size, player_name=player_name)
