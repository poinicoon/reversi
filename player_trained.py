import numpy as np

import player_base


class PlayerTrained(player_base.PlayerBase):
    def execute_(self, raw_field: np.ndarray) -> np.ndarray:
        put_coord_list = []  # type: typing.List[np.ndarray]

    def __init__(self, player_num: int, player_name="Trained"):
        super(PlayerTrained, self).__init__(player_num, player_name=player_name)
