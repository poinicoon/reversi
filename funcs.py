import numpy as np
from itertools import product


def GetValue(field, coord):
    return int(field[coord[0], coord[1]])


def GetNextPlayer(player_num):
    if player_num == 0:
        return 1
    elif player_num == 1:
        return 0
    else:
        return -1


def GetCornerCoord(field_size, corner_num):
    if corner_num == 0:
        return (0, 0)
    elif corner_num == 1:
        return (0, field_size[1] - 1)
    elif corner_num == 2:
        return (field_size[0] - 1, 0)
    elif corner_num == 3:
        return (field_size[0] - 1, field_size[1] - 1)


def GetCenterCoord(field_size, center_num):
    if center_num == 0:
        return (field_size[0] // 2 - 1, field_size[1] // 2 - 1)
    elif center_num == 1:
        return (field_size[0] // 2 - 1, field_size[1] // 2)
    elif center_num == 2:
        return (field_size[0] // 2, field_size[1] // 2 - 1)
    elif center_num == 3:
        return (field_size[0] // 2, field_size[1] // 2)


def GetMovedCoord(coord, direc_num, move_size):
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
    return -1 < coord[0] and coord[0] < field_size[0] and -1 < coord[1] and coord[1] < field_size[1]


def GetNumOfPlayerPosition(field, player_num):
    return field[field == player_num].size


def IsEmptyCoordExist(field):
    return 0 < GetNumOfPlayerPosition(field, -1)


def GetMostPlayerNumber(field):
    num_of_pos = (GetNumOfPlayerPosition(field, 0), GetNumOfPlayerPosition(field, 1))

    if num_of_pos[1] < num_of_pos[0]:
        return 0
    elif num_of_pos[0] < num_of_pos[1]:
        return 1
    else:
        return 2


def GetGettablePositionList(field, put_coord, player_num):
    enemy_player_num = GetNextPlayer(player_num)
    empty = -1
    field_max = np.max(field.shape)

    coord_list = []

    for direc_num in range(8):

        for move_size in range(field_max):
            tmp_coord = GetMovedCoord(put_coord, direc_num, move_size)
            if IsCoordInRange(field.shape, tmp_coord):
                value = GetValue(field, tmp_coord)
                if move_size == 0:
                    if not value == empty:
                        break
                elif move_size == 1:
                    if not value == enemy_player_num:
                        break
                else:
                    if value == empty:
                        break
                    elif value == player_num:
                        if len(coord_list) == 0:
                            coord_list.append(put_coord)
                        for move_size2 in range(1, move_size + 1):
                            coord_list.append(GetMovedCoord(put_coord, direc_num, move_size2))
                        break
            else:
                break

    '''
    if IsCoordInRange(field.shape, put_coord) and GetValue(field, put_coord) == -1:
        for direc_num in range(8):
            tmp_coord = GetMovedCoord(put_coord, direc_num, 1)
            if IsCoordInRange(field.shape, tmp_coord) and GetValue(field, tmp_coord) == enemy_player_num:
                for move_size in range(2, field_max):
                    tmp_coord = GetMovedCoord(put_coord, direc_num, move_size)
                    if IsCoordInRange(field.shape, tmp_coord):
                        if GetValue(field, tmp_coord) == -1:
                            break
                        elif GetValue(field, tmp_coord) == player_num:
                            print("eeeeeeee")
                            if len(coord_list) == 0:
                                coord_list.append(put_coord)
                            for move_size2 in range(1, move_size + 1):
                                coord_list.append(GetMovedCoord(put_coord, direc_num, move_size2))
                            break
    '''
    return coord_list


def GetNumOfGettablePosition(field, coord, player_num):
    return len(GetGettablePositionList(field, coord, player_num))


def IsCoordValid(field, coord, player_num):
    return 0 < GetNumOfGettablePosition(field, coord, player_num)


def IsPuttableCoordExist(field, player_num):
    for coord in product(range(field.shape[0]), range(field.shape[1])):
        if IsCoordValid(field, coord, player_num):
            return True
    return False


def GetCoordNum(field_size, coord):
    coord_num = np.zeros(field_size)
    coord_num[coord[0], coord[1]] = 1
    coord_num = coord_num.reshape([-1])
    return coord_num


def GetField3dimOnehot(field):
    field3 = np.zeros([field.shape[0], field.shape[1], 3])

    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        field3[col, row, GetValue(field, np.array([col, row])) + 1] = 1

    return field3


def RestoreField(field):
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
    field = RestoreField(field)
    coord = np.zeros(field.shape)
    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        if IsCoordValid(field, np.array([col, row]), 1):
            coord[col, row] = 1
    coord = coord.reshape([-1])  # flatten
    return coord


def ReversePlayernumField(field):
    field = np.empty(field.shape)
    for col, row in product(range(field.shape[0]), range(field.shape[1])):
        field[col, row] = GetNextPlayer(field[col, row])
    return field


def Softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
