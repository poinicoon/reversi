import numpy as np

from funcs import GetCoordNum, GetField3dimOnehot, GetNextPlayer, GetNumOfPlayerPosition
from field import Field
from player_base import PlayerBase


class Game:
    __field = None  # type: Field
    __players = (None, None)  # type: (PlayerBase)

    __current_player_num = None  # type: int
    __num_of_turn = None  # type: int

    __datasets_field = []  # type: [np.ndarray]
    __datasets_coord = []  # type: [np.ndarray]

    __is_show_game = False

    def reverse_player(self) -> None:
        self.__current_player_num = GetNextPlayer(self.__current_player_num)

    def increment_turn(self) -> None:
        self.__num_of_turn += 1

    def print(self, values=None, end=None) -> None:
        if self.__is_show_game:
            print("" if values is None else values, end=end)

    def start(self) -> (int, [np.ndarray], [np.ndarray]):

        def print(values):
            self.print(values)

        print("Game start.")

        # 両プレイヤーの置く場所が無くなるまでループ
        while self.__field.is_puttable_coord_exist(0) or self.__field.is_puttable_coord_exist(1):
            put_result = False

            # 現在のプレイヤーが置けない場合パス処理
            if not self.__field.is_puttable_coord_exist(self.__current_player_num):
                self.__players[self.__current_player_num].pass_(self.__field.get_field)  # プレイヤーに対してパスを宣告
                self.reverse_player()  # 次のプレイヤーに
                continue

            self.print("Turn: " + str(self.__num_of_turn))
            self.print("Player: " + str(self.__current_player_num))
            self.print(self.__field.get_field().astype('int') + 1)

            # プレイヤーに対して座標を訪ねる
            while (not put_result):
                put_coord = self.__players[self.__current_player_num].execute_(self.__field.get_field())
                tmp_field = self.__field.get_field()
                put_result = self.__field.put(put_coord, self.__current_player_num)

                self.print(str(put_coord[0]) + ", " + str(put_coord[1]) + " -> " + str(put_result))

                if put_result:
                    self.__players[self.__current_player_num].result_(True)
                    if self.__current_player_num == 1:
                        self.__datasets_field.append(GetField3dimOnehot(tmp_field))
                        self.__datasets_coord.append(GetCoordNum(self.__field.get_field_size(), put_coord))
                else:
                    self.__players[self.__current_player_num].result_(False)

            self.print(self.__field.get_field().astype('int') + 1)
            self.print("0: " + str(GetNumOfPlayerPosition(self.__field.get_field(), 0)))
            self.print("1: " + str(GetNumOfPlayerPosition(self.__field.get_field(), 1)))
            self.print()

            # 次のターン
            self.reverse_player()
            self.increment_turn()

        winner = self.__field.get_most_player_number()

        self.__players[0].end_(self.__field.get_field(), winner)
        self.__players[1].end_(self.__field.get_field(), winner)

        return winner, self.__datasets_field, self.__datasets_coord

    def __init__(self, field: Field, players: (PlayerBase, PlayerBase), fields: [np.ndarray],
                 coords: [np.ndarray], show=False) -> None:
        self.__field = field
        self.__players = players

        self.__current_player_num = np.random.randint(2)
        self.__num_of_turn = 1

        self.__datasets_field = fields
        self.__datasets_coord = coords

        self.__is_show_game = show
