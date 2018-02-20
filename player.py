import numpy as np
from itertools import product
from keras.models import load_model
from funcs import IsCoordValid, GetNumOfGettablePosition, GetField3dimOnehot


# プレイヤープログラムの基底クラス
class Player:
    __player_num = None  # type: int
    __player_name = None  # type: str
    __field_size = None  # type: np.ndarray

    def execute_(self, field: np.ndarray) -> np.ndarray:
        return np.empty([2])

    def result_(self, result: bool) -> None:
        return

    def pass_(self, field: np.ndarray) -> None:
        return

    def get_player_number(self) -> int:
        return self.__player_num

    def get_player_name(self) -> str:
        return self.__player_name

    def get_field_size(self) -> np.ndarray:
        return self.__field_size

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Player") -> None:
        self.__player_num = player_num
        self.__player_name = player_name
        self.__field_size = field_size


# プレイヤーが直接入力するプレイヤープログラム
class PlayerHuman(Player):
    def execute_(self, field: np.ndarray) -> np.ndarray:
        print("col >>> ", end="")
        col = int(input())
        print("row >>> ", end="")
        row = int(input())
        return np.array([col, row])

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Human") -> None:
        super(PlayerHuman, self).__init__(player_num, field_size, player_name=player_name)


# 石を置ける座標をランダムに決定するプレイヤープログラム
class PlayerRandom(Player):
    def execute_(self, field: np.ndarray) -> np.ndarray:

        put_coord_list = []  # type: [np.ndarray]

        for col, row in product(range(field.shape[0]), range(field.shape[1])):
            tmp_coord = np.array([col, row])
            if IsCoordValid(field, tmp_coord, self.get_player_number()):
                put_coord_list.append(tmp_coord)

        return put_coord_list[np.random.randint(len(put_coord_list))]

    def __init__(self, player_num: int, field_size: np.array, *, player_name="RandomValidOnly") -> None:
        super(PlayerRandom, self).__init__(player_num, field_size, player_name=player_name)


# 取れる石数が最大になる座標を指定するプレイヤープログラム
class PlayerMax(Player):
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


# 訓練済みモデルから石を置く座標を決定するプレイヤープログラム
class PlayerTrained(Player):
    model = None

    def execute_(self, field):
        field_size = self.get_field_size()
        coord_list = self.model.predict(GetField3dimOnehot(field))

        coord_max = np.max(coord_list)
        coord_list = [i for i in coord_list[0] if coord_max == i]

        coord = coord_list[np.random.randint(len(coord_list))]
        coord = np.array([np.round(coord / field_size[1]), coord - np.round(coord / field_size[1]) * field_size[1]])

        return coord

    def __init__(self, player_num, field_size, player_name="Trained"):
        super(PlayerTrained, self).__init__(player_num, field_size, player_name=player_name)

        model_path = "~/.reversi_nn/model.h5"
        self.model = load_model(model_path)
