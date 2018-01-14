import numpy as np
from keras.models import Sequential, load_model

from config import ModelPath
from player_base import PlayerBase
from funcs import GetField3dimOnehot


class PlayerTrained(PlayerBase):
    model = None  # type: Sequential

    def execute_(self, field: np.ndarray) -> np.ndarray:
        field_size = self.get_field_size()
        coord_list = self.model.predict(GetField3dimOnehot(field))

        coord_avg = np.average(coord_list)
        coord_list = [i for i in coord_list[0] if coord_avg < i]

        coord = coord_list[np.random.randint(len(coord_list))]
        coord = np.array([np.round(coord / field_size[1]), coord - np.round(coord / field_size[1]) * field_size[1]])

        return coord

    def __init__(self, player_num: int, field_size: np.ndarray, player_name="Trained") -> None:
        super(PlayerTrained, self).__init__(player_num, field_size, player_name=player_name)

        self.model = load_model(ModelPath)
