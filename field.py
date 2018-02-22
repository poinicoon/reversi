'''
盤面を管理するプログラム。
'''

import numpy as np

from funcs import IsCoordInRange, IsEmptyCoordExist, IsCoordValid, IsPuttableCoordExist, GetNumOfPlayerPosition, \
    GetMostPlayerNumber, GetGettablePositionList, GetNumOfGettablePosition, GetCenterCoord, GetNextPlayer


class Field:
    __field = None

    def __set_value(self, coord, value):
        self.__field[coord[0], coord[1]] = value

    def get_value(self, coord):
        return int(self.__field[coord[0], coord[1]])

    def get_field(self):
        return self.__field

    def get_field_size(self):
        return self.__field.shape

    def is_coord_in_range(self, coord):
        return IsCoordInRange(self.__field, coord)

    def is_empty_coord_exist(self):
        return IsEmptyCoordExist(self.__field)

    def is_coord_valid(self, coord, player_num):
        return IsCoordValid(self.__field, coord, player_num)

    def is_puttable_coord_exist(self, player_num):
        return IsPuttableCoordExist(self.__field, player_num)

    def get_num_of_player_position(self, player_num):
        return GetNumOfPlayerPosition(self.__field, player_num)

    def get_most_player_number(self):
        return GetMostPlayerNumber(self.__field)

    def get_gettable_position_list(self, coord, player_num):
        return GetGettablePositionList(self.__field, coord, player_num)

    def get_num_of_gettable_position(self, coord, player_num):
        return GetNumOfGettablePosition(self.__field, coord, player_num)

    def put(self, coord, player_num):
        if self.is_coord_valid(coord, player_num):
            put_coord_list = self.get_gettable_position_list(coord, player_num)
            for i in range(len(put_coord_list)):
                self.__set_value(put_coord_list[i], player_num)
            return True
        else:
            return False

    def __init__(self, field_size):
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
