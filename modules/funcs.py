# -*- coding: utf-8 -*-

"""
関数
"""

import numpy as np
from itertools import product


def GetValue(field, coord):
    """
    盤面の値を返す。
    :param field: 盤面
    :param coord: 座標
    :return: 値
    """
    return int(field[coord[0], coord[1]])


def GetNextPlayer(player_num):
    """
    次のプレイヤー番号を返す。
    :param player_num: プレイヤー番号
    :return: 次のプレイヤー番号
    """
    if player_num == 0:
        return 1
    elif player_num == 1:
        return 0
    else:
        return -1


def GetCornerCoord(field_size, corner_num):
    """
    盤面の角の座標を返す。
    :param field_size: 盤面サイズ
    :param corner_num: 角番号
    :return: 座標
    """
    if corner_num == 0:
        return (0, 0)
    elif corner_num == 1:
        return (0, field_size[1] - 1)
    elif corner_num == 2:
        return (field_size[0] - 1, 0)
    elif corner_num == 3:
        return (field_size[0] - 1, field_size[1] - 1)


def GetCenterCoord(field_size, center_num):
    """
    盤面の中央の座標を返す。
    :param field_size: 盤面サイズ
    :param center_num: 中心番号
    :return: 座標
    """
    if center_num == 0:
        return (field_size[0] // 2 - 1, field_size[1] // 2 - 1)
    elif center_num == 1:
        return (field_size[0] // 2 - 1, field_size[1] // 2)
    elif center_num == 2:
        return (field_size[0] // 2, field_size[1] // 2 - 1)
    elif center_num == 3:
        return (field_size[0] // 2, field_size[1] // 2)


def GetMovedCoord(coord, direc_num, move_size):
    """
    移動後の座標を返す。
    :param coord: 座標
    :param direc_num: 方向
    :param move_size: 移動サイズ
    :return: 移動後サイズ
    """
    if direc_num == 0:
        return (coord[0] - move_size, coord[1] - move_size)
    elif direc_num == 1:
        return (coord[0] - move_size, coord[1])
    elif direc_num == 2:
        return (coord[0] - move_size, coord[1] + move_size)
    elif direc_num == 3:
        return (0, coord[1] - move_size)
    elif direc_num == 4:
        return (0, coord[1] + move_size)
    elif direc_num == 5:
        return (coord[0] + move_size, coord[1] - move_size)
    elif direc_num == 6:
        return (coord[0] + move_size, coord[1])
    elif direc_num == 7:
        return (coord[0] + move_size, coord[1] + move_size)


def IsCoordInRange(field_size, coord):
    """
    座標が盤面内かどうか判定する。
    :param field_size: 盤面サイズ
    :param coord: 座標
    :return: 真偽値
    """
    return -1 < coord[0] and coord[0] < field_size[0] and -1 < coord[1] and coord[1] < field_size[1]


def GetNumOfPlayerPosition(field, player_num):
    """
    プレイヤーの所持している石の数を返す。
    :param field: 盤面
    :param player_num: プレイヤー番号
    :return: 石の数
    """
    return field[field == player_num].size


def IsEmptyCoordExist(field):
    """
    盤面に空き座標が存在するか判定
    :param field: 盤面
    :return: 真偽値
    """
    return 0 < GetNumOfPlayerPosition(field, -1)


def GetMostPlayerNumber(field):
    """
    所持している石の数が一番多いプレイヤー番号を返す。
    :param field: 盤面
    :return: プレイヤー番号
    """
    num_of_pos = (GetNumOfPlayerPosition(field, 0), GetNumOfPlayerPosition(field, 1))

    if num_of_pos[1] < num_of_pos[0]:
        return 0
    elif num_of_pos[0] < num_of_pos[1]:
        return 1
    else:
        return 2


def GetGettableCoordList(field, put_coord, player_num):
    """
    指定座標で取得可能な座標リストを返す。
    :param field: 盤面
    :param put_coord: 座標
    :param player_num: プレイヤー番号
    :return: 座標リスト
    """
    enemy_player_num = GetNextPlayer(player_num)
    field_max = max(field.shape)

    coord_list = []

    for direc_num in range(8):

        for move_size in range(field_max):
            tmp_coord = GetMovedCoord(put_coord, direc_num, move_size)
            if IsCoordInRange(field.shape, tmp_coord):
                value = GetValue(field, tmp_coord)
                if move_size == 0:
                    if not value == -1:
                        break
                elif move_size == 1:
                    if not value == enemy_player_num:
                        break
                else:
                    if value == -1:
                        break
                    elif value == player_num:
                        if len(coord_list) == 0:
                            coord_list.append(put_coord)
                        for move_size2 in range(1, move_size + 1):
                            coord_list.append(GetMovedCoord(put_coord, direc_num, move_size2))
                        break
            else:
                break
    return coord_list


def GetNumOfGettablePosition(field, coord, player_num):
    """
    指定座標で取得可能な石の数を返す。
    :param field: 盤面
    :param coord: 座標
    :param player_num: プレイヤー番号
    :return: 石の数
    """
    return len(GetGettableCoordList(field, coord, player_num))


def IsCoordValid(field, coord, player_num):
    """
    指定座標が有効かどうか判定する。
    :param field: 盤面
    :param coord: 座標
    :param player_num: プレイヤー番号
    :return: 真偽値
    """
    return 0 < GetNumOfGettablePosition(field, coord, player_num)


def IsPuttableCoordExist(field, player_num):
    """
    石を置ける座標が存在するか判定する。
    :param field: 盤面
    :param player_num: プレイヤー番号
    :return: 真偽値
    """
    for coord in product(range(field.shape[0]), range(field.shape[1])):
        if IsCoordValid(field, coord, player_num):
            return True
    return False


def GetCoordNum(field_size, coord):
    """

    :param field_size:
    :param coord:
    :return:
    """
    coord_num = np.zeros(field_size)
    coord_num[coord[0], coord[1]] = 1
    coord_num = coord_num.reshape([-1])
    return coord_num


def Field1ToField2(field):
    field3 = np.zeros([field.shape[0], field.shape[1], 3])

    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        field3[col, row, GetValue(field, np.array([col, row])) + 1] = 1

    return field3


def Field2ToField1(field):
    field2 = np.zeros([field.shape[0], field.shape[1]])

    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        if field[col, row, 1] == 1:
            field2[col, row] = 0
        elif field[col, row, 2] == 1:
            field2[col, row] = 1
        else:
            field2[col, row] = -1

    return field2


def GetTestCoord(field):
    field = Field2ToField1(field)
    coord = np.zeros(field.shape)
    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        if IsCoordValid(field, np.array([col, row]), 1):
            coord[col, row] = 1
    coord = coord.reshape([-1])  # flatten
    return coord


def ReversePlayerNumInField(field):
    field = np.empty(field.shape)
    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        field[col, row] = GetNextPlayer(field[col, row])
    return field


def Softmax(x):
    x = np.exp(x)
    return x / np.sum(x)
