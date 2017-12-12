import numpy as np

import player_base


class PlayerRandomAll(player_base.PlayerBase):
    def execute_(self, raw_field: np.ndarray) -> np.ndarray:
        return np.array([np.random.randint(raw_field.shape[0]), np.random.randint(raw_field.shape[1])])

    def __init__(self, player_num: int, field_size: np.array, *, player_name="RandomAll"):
        super(PlayerRandomAll, self).__init__(player_num, field_size, player_name=player_name)
