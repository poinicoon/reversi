# -*- coding: utf-8 -*-

"""
盤面を管理するプログラム。
"""

import numpy as np

from modules.funcs import IsCoordInRange, IsEmptyCoordExist, IsCoordValid, IsPuttableCoordExist, GetNumOfPlayerPosition, \
    GetMostPlayerNumber, GetGettableCoordList, GetNumOfGettablePosition, GetCenterCoord, GetNextPlayer


class Field:
    __field = None
    """
    盤面
    """

    def __set_value(self, coord, value):
        """
        盤面に値をセットする関数。
        :param coord: 値をセットする座標
        :param value: セットする値
        :return: なし
        """
        self.__field[coord[0], coord[1]] = value

    def get_value(self, coord):
        """
        盤面の指定座標の値を返す。
        :param coord: 座標
        :return: 指定座標の値
        """
        return int(self.__field[coord[0], coord[1]])

    def get_field(self):
        """
        盤面データを返す。
        :return: 盤面
        """
        return self.__field

    def get_field_size(self):
        """
        盤面サイズを返す。
        :return: 盤面サイズ
        """
        return self.__field.shape

    def is_coord_in_range(self, coord):
        """
        座標が盤面内か判定する。
        :param coord: 座標
        :return: 真偽値
        """
        return IsCoordInRange(self.__field, coord)

    def is_empty_coord_exist(self):
        """
        空き座標があるか判定する。
        :return: 真偽値
        """
        return IsEmptyCoordExist(self.__field)

    def is_coord_valid(self, coord, player_num):
        """
        座標が有効かどうか判定する。
        :param coord: 座標
        :param player_num: プレイヤー番号
        :return: 真偽値
        """
        return IsCoordValid(self.__field, coord, player_num)

    def is_puttable_coord_exist(self, player_num):
        """
        石を置ける座標が存在するか判定する。
        :param player_num: プレイヤー番号
        :return: 真偽値
        """
        return IsPuttableCoordExist(self.__field, player_num)

    def get_num_of_player_position(self, player_num):
        """
        プレイヤーが所持している石の数を返す。
        :param player_num: プレイヤー番号
        :return: 石の数
        """
        return GetNumOfPlayerPosition(self.__field, player_num)

    def get_most_player_number(self):
        """
        石の数が一番多いプレイヤー番号を返す。
        :return: プレイヤー番号
        """
        return GetMostPlayerNumber(self.__field)

    def get_gettable_coord_list(self, coord, player_num):
        """
        指定座標で取れる石の座標を返す。
        :param coord: 座標
        :param player_num: プレイヤー番号
        :return: 座標リスト
        """
        return GetGettableCoordList(self.__field, coord, player_num)

    def get_num_of_gettable_position(self, coord, player_num):
        """
        指定座標で取れる石の数を返す。
        :param coord: 座標
        :param player_num: プレイヤー番号
        :return: 石の数
        """
        return GetNumOfGettablePosition(self.__field, coord, player_num)

    def put(self, coord, player_num):
        """
        石を置く。
        :param coord: 座標
        :param player_num: プレイヤー番号
        :return: 真偽値
        """
        if self.is_coord_valid(coord, player_num):
            put_coord_list = self.get_gettable_coord_list(coord, player_num)
            for i in range(len(put_coord_list)):
                self.__set_value(put_coord_list[i], player_num)
            return True
        else:
            return False

    def __init__(self, field_size):
        """
        初期化
        :param field_size: 盤面サイズ
        """
        ul = GetCenterCoord(field_size, 0)
        ur = GetCenterCoord(field_size, 1)
        dl = GetCenterCoord(field_size, 2)
        dr = GetCenterCoord(field_size, 3)

        self.__field = np.empty(field_size)
        self.__field.fill(-1)

        self.__set_value(ul, np.random.randint(2))
        self.__set_value(ur, GetNextPlayer(self.get_value(ul)))
        self.__set_value(dl, self.get_value(ur))
        self.__set_value(dr, self.get_value(ul))
