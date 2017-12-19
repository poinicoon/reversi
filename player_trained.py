import json
import numpy as np
from keras.models import Sequential, load_model

import player_base
from funcs import GetField3dimOnehot

config = json.load(open("config.json", "r"))


class PlayerTrained(player_base.PlayerBase):
    model = None  # type: Sequential

    def execute_(self, field: np.ndarray) -> np.ndarray:
        coord_list = self.model.predict(GetField3dimOnehot(field))  # type: np.ndarray
        coord_avg = np.average(coord_list)
        coord_list = [i for i in coord_list[0] if coord_avg < i]
        return coord_list[np.random.randint(len(coord_list))]

    def __init__(self, player_num: int, field_size: np.ndarray, player_name="Trained"):
        super(PlayerTrained, self).__init__(player_num, field_size, player_name=player_name)

        self.model = load_model(config["model_path"])
