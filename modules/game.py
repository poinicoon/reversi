"""
ゲームの進行を管理するプログラム。
直接起動せずに、プログラムから呼び出す。
"""

import numpy as np

from modules.funcs import GetCoordNum, Field1ToField2, GetNextPlayer, GetNumOfPlayerPosition


class Game:
    __is_stdout = None

    __field = None
    __players = (None, None)

    __current_player_num = None
    __num_of_turn = None

    __x = None
    __y = None

    def __reverse_player(self):
        self.__current_player_num = GetNextPlayer(self.__current_player_num)

    def __increment_turn(self):
        self.__num_of_turn += 1

    def start(self):
        '''
        ゲーム開始
        :return: 勝者のプレイヤー番号, X, Y
        '''

        if self.__is_stdout:
            print("Game start.")

        # 両プレイヤーの置く場所が無くなるまでループ
        while self.__field.is_puttable_coord_exist(0) or self.__field.is_puttable_coord_exist(1):
            put_result = False

            # 現在のプレイヤーが置けない場合パス処理
            if not self.__field.is_puttable_coord_exist(self.__current_player_num):
                self.__players[self.__current_player_num].pass_(self.__field.get_field)  # プレイヤーに対してパスを宣告
                self.__reverse_player()  # 次のプレイヤーに
                continue

            if self.__is_stdout:
                print("Turn: " + str(self.__num_of_turn))
                print("Player: " + str(self.__current_player_num))
                print(self.__field.get_field().astype('int') + 1)

            # プレイヤーに対して座標を訪ねる
            while (not put_result):
                put_coord = self.__players[self.__current_player_num].execute_(self.__field.get_field())
                tmp_field = self.__field.get_field()
                put_result = self.__field.put(put_coord, self.__current_player_num)

                if self.__is_stdout:
                    print(put_coord, end=" -> ")
                    print(put_result)

                if put_result:
                    self.__players[self.__current_player_num].result_(True)
                    if self.__current_player_num == 1:
                        self.__x.append(Field1ToField2(tmp_field))
                        self.__y.append(GetCoordNum(self.__field.get_field_size(), put_coord))
                else:
                    self.__players[self.__current_player_num].result_(False)

            if self.__is_stdout:
                print(self.__field.get_field().astype('int') + 1)
                print("0: " + str(GetNumOfPlayerPosition(self.__field.get_field(), 0)))
                print("1: " + str(GetNumOfPlayerPosition(self.__field.get_field(), 1)))
                print()

            # 次のターン
            self.__reverse_player()
            self.__increment_turn()

        winner = self.__field.get_most_player_number()

        return winner, np.array(self.__x), np.array(self.__y)

    def __init__(self, field, players, stdout=True):
        '''
        初期化する。
        :param field: 盤面
        :param players: プレイヤーを格納したタプル
        '''

        self.__is_stdout = stdout

        self.__field = field
        self.__players = players

        self.__current_player_num = np.random.randint(2)
        self.__num_of_turn = 1

        self.__x = []
        self.__y = []
