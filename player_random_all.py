import numpy as np

from player_base import PlayerBase


class PlayerRandomAll(PlayerBase):
    def execute_(self, field: np.ndarray) -> np.ndarray:
        return np.array([np.random.randint(field.shape[0]), np.random.randint(field.shape[1])])

    def __init__(self, player_num: int, field_size: np.array, *, player_name="RandomAll") -> None:
        super(PlayerRandomAll, self).__init__(player_num, field_size, player_name=player_name)
