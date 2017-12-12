import numpy as np

import funcs
import field
import player_base


class Game:
    __field = None  # type: field.Field
    __players = (None, None)  # type: (player_base.PlayerBase)

    __current_player_num = -1  # type: int
    __num_of_turn = -1  # type: int

    __datasets_field = []  # type: [np.ndarray]
    __datasets_coord = []  # type: [np.ndarray]

    def reverse_player(self) -> None:
        self.__current_player_num = funcs.get_next_player(self.__current_player_num)

    def increment_turn(self) -> None:
        self.__num_of_turn += 1

    def start(self) -> (int, [np.ndarray], [np.ndarray]):

        # 両プレイヤーの置く場所が無くなるまでループ
        while self.__field.is_puttable_coord_exist(0) or self.__field.is_puttable_coord_exist(1):
            # 現在のプレイヤーが置けない場合パス処理
            if not self.__field.is_puttable_coord_exist(self.__current_player_num):
                self.__players[self.__current_player_num].pass_(self.__field.get_raw_field)  # プレイヤーに対してパスを宣告
                self.reverse_player()  # 次のプレイヤーに
                continue

            # プレイヤーに対して座標を訪ねる
            put_coord = self.__players[self.__current_player_num].execute_(
                self.__field.get_raw_field())  # type: np.ndarray
            tmp_coord = put_coord
            tmp_field = self.__field.get_raw_field()

            # 置き、その結果を取得
            put_result = self.__field.put(put_coord, self.__current_player_num)  # type: bool

            while (not put_result):
                self.__players[self.__current_player_num].result_(False)
                put_coord = self.__players[self.__current_player_num].execute_(self.__field.get_raw_field())
                tmp_coord = put_coord
                tmp_field = self.__field.get_raw_field()
                put_result = self.__field.put(put_coord, self.__current_player_num)

            self.__players[self.__current_player_num].result_(True)

            # field ndim=2 -> ndim=3
            tmp_field_2 = funcs.field_ndim_2_to_3(tmp_field)

            # vector to number
            tmp_coord_2 = funcs.coord_to_num(self.__field.get_field_size(), tmp_coord)
            # tmp_coord_2 = funcs.coord_to_3dim(self.__field.get_field_size(), tmp_coord, self.__current_player_num)

            # データセットに追加
            self.__datasets_field.append(tmp_field_2)
            self.__datasets_coord.append(tmp_coord_2)

            # 次のターン
            self.reverse_player()
            self.increment_turn()

        winner = self.__field.get_most_player_number()  # type: int

        self.__players[0].end_(self.__field.get_raw_field(), winner)
        self.__players[1].end_(self.__field.get_raw_field(), winner)

        return winner, self.__datasets_field, self.__datasets_coord

    def __init__(self, field_ins: field.Field, players_ins: (player_base.PlayerBase, player_base.PlayerBase),
                 fields: [np.ndarray],
                 coords: [np.ndarray]):
        self.__field = field_ins
        self.__players = players_ins

        self.__current_player_num = funcs.generate_random(0, 1)
        self.__num_of_turn = 1

        self.__datasets_field = fields
        self.__datasets_coord = coords
