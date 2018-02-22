# -*- coding: utf-8 -*-

import numpy as np
from itertools import product
from keras.models import load_model
from modules.funcs import IsCoordValid, GetNumOfGettablePosition, Field1ToField2


class Player:
    """
    プレイヤープログラムの基底クラス
    """
    __player_num = None
    __player_name = None
    __field_size = None

    def execute_(self, field):
        return (-1, -1)

    def result_(self, result):
        return

    def pass_(self, field):
        return

    def get_player_number(self):
        return self.__player_num

    def get_player_name(self):
        return self.__player_name

    def get_field_size(self):
        return self.__field_size

    def __init__(self, player_num, field_size, player_name="Player"):
        self.__player_num = player_num
        self.__player_name = player_name
        self.__field_size = field_size


class PlayerHuman(Player):
    """
    プレイヤーが直接入力するプレイヤープログラム
    """

    def execute_(self, field):
        print("col >>> ", end="")
        col = int(input())
        print("row >>> ", end="")
        row = int(input())
        return np.array([col, row])

    def __init__(self, player_num: int, field_size: np.array, player_name="Human"):
        super(PlayerHuman, self).__init__(player_num, field_size, player_name=player_name)


class PlayerRandom(Player):
    """
    石を置ける座標をランダムに決定するプレイヤープログラム
    """

    def execute_(self, field):

        put_coord_list = []

        for col, row in product(range(field.shape[0]), range(field.shape[1])):
            tmp_coord = np.array([col, row])
            if IsCoordValid(field, tmp_coord, self.get_player_number()):
                put_coord_list.append(tmp_coord)

        return put_coord_list[np.random.randint(len(put_coord_list))]

    def __init__(self, player_num: int, field_size: np.array, player_name="RandomValidOnly"):
        super(PlayerRandom, self).__init__(player_num, field_size, player_name=player_name)


class PlayerMax(Player):
    """
    取れる石数が最大になる座標を指定するプレイヤープログラム
    """

    def execute_(self, field):

        max_num = 0
        max_pos = None

        for col, row in product(range(field.shape[0]), range(field.shape[1])):
            tmp_num = GetNumOfGettablePosition(field, np.array([col, row]), self.get_player_number())
            if max_num < tmp_num:
                max_num = tmp_num
                max_pos = np.array([col, row])

        return max_pos

    def __init__(self, player_num: int, field_size: np.array, player_name="Max"):
        super(PlayerMax, self).__init__(player_num, field_size, player_name=player_name)


class PlayerTrained(Player):
    """
    訓練済みモデルから石を置く座標を決定する
    """
    model = None

    def execute_(self, field):
        field_size = self.get_field_size()
        coord_list = self.model.predict(Field1ToField2(field))

        coord_max = np.max(coord_list)
        coord_list = [i for i in coord_list[0] if coord_max == i]

        coord = coord_list[np.random.randint(len(coord_list))]
        coord = np.array([np.round(coord / field_size[1]), coord - np.round(coord / field_size[1]) * field_size[1]])

        return coord

    def __init__(self, player_num, field_size, player_name="Trained"):
        super(PlayerTrained, self).__init__(player_num, field_size, player_name=player_name)

        model_path = "$HOME/.reversi_nn/model.h5"
        self.model = load_model(model_path)
