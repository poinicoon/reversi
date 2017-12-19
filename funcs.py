import numpy as np


def GetValue(field: np.ndarray, coord: np.ndarray) -> int:
    coord = coord.astype('int')
    field = field.astype('int')
    return field[coord[0], coord[1]]


def GetNextPlayer(player_num: int) -> int:
    if player_num == 0:
        return 1
    elif player_num == 1:
        return 0
    else:
        return -1


def GetCornerCoord(field_size: np.ndarray, corner_num: int) -> np.ndarray:
    if corner_num == 0:
        return np.array([0, 0])
    elif corner_num == 1:
        return field_size - np.array([0, 1])
    elif corner_num == 2:
        return field_size - np.array([1, 0])
    elif corner_num == 3:
        return field_size - 1
    else:
        return np.array([-1, -1])


def GetCenterCoord(field_size: np.ndarray, center_num: int) -> np.ndarray:
    if center_num == 0:
        return field_size / 2 - np.array([1, 1])
    elif center_num == 1:
        return field_size / 2 - np.array([1, 0])
    elif center_num == 2:
        return field_size / 2 - np.array([0, 1])
    elif center_num == 3:
        return field_size / 2
    else:
        return np.array([-1, -1])


def GetMovedCoord(coord: np.ndarray, direc_num: int, move_size: int) -> np.ndarray:
    if direc_num == 0:
        return np.array([-move_size, -move_size]) + coord
    elif direc_num == 1:
        return np.array([-move_size, 0]) + coord
    elif direc_num == 2:
        return np.array([-move_size, move_size]) + coord
    elif direc_num == 3:
        return np.array([0, -move_size]) + coord
    elif direc_num == 4:
        return np.array([0, move_size]) + coord
    elif direc_num == 5:
        return np.array([move_size, -move_size]) + coord
    elif direc_num == 6:
        return np.array([move_size, 0]) + coord
    elif direc_num == 7:
        return np.array([move_size, move_size]) + coord
    else:
        return np.array([0, 0]) + coord


def IsCoordInRange(field_size: np.ndarray, coord: np.ndarray) -> bool:
    return (coord < field_size)[0] and (coord < field_size)[1]


def GetNumOfPlayerPosition(field: np.ndarray, player_num: int) -> int:
    return field[field == player_num].size


def IsEmptyCoordExist(raw_field: np.ndarray) -> bool:
    return 0 < GetNumOfPlayerPosition(raw_field, -1)


def GetMostPlayerNumber(raw_field: np.ndarray) -> int:
    num_of_pos = (GetNumOfPlayerPosition(raw_field, 0), GetNumOfPlayerPosition(raw_field, 1))

    if num_of_pos[1] < num_of_pos[0]:
        return 0
    elif num_of_pos[0] < num_of_pos[1]:
        return 1
    else:
        return 2


def GetGettablePositionList(field: np.ndarray, put_coord: np.ndarray, player_num: int) -> [np.ndarray]:
    next_player_num = GetNextPlayer(player_num)
    field_max = np.max(field.shape)
    gettable_pos_list = []  # type: [np.ndarray]

    # coord is not empty
    if GetValue(field, put_coord) != -1:
        return gettable_pos_list

    # coord is out of field
    if not (IsCoordInRange(np.array(field.shape), put_coord)):
        return gettable_pos_list

    for direc_num in range(8):
        tmp_coord = GetMovedCoord(put_coord, direc_num, 1)  # type: np.ndarray
        if not (IsCoordInRange(np.array(field.shape), tmp_coord)):
            continue

        # next position is not next player
        tmp_coord = GetMovedCoord(put_coord, direc_num, 1)
        if GetValue(field, tmp_coord) != next_player_num:
            continue

        for move_size in range(2, field_max):
            tmp_coord = GetMovedCoord(put_coord, direc_num, move_size)  # type: np.ndarray

            if not (IsCoordInRange(np.array(field.shape), tmp_coord)):
                break

            if GetValue(field, tmp_coord) == next_player_num:
                continue

            if GetValue(field, tmp_coord) == player_num:
                if len(gettable_pos_list) == 0:
                    gettable_pos_list.append(put_coord)

                for move_size2 in range(1, move_size + 1):
                    tmp_coord = GetMovedCoord(put_coord, direc_num, move_size2)
                    gettable_pos_list.append(tmp_coord)

                break

            if GetValue(field, tmp_coord) == -1:
                break

    return gettable_pos_list


def GetNumOfGettablePosition(raw_field: np.ndarray, coord: np.ndarray, player_num: int) -> int:
    return len(GetGettablePositionList(raw_field, coord, player_num))


def IsCoordValid(raw_field: np.ndarray, coord: np.ndarray, player_num: int) -> bool:
    return bool(0 < GetNumOfGettablePosition(raw_field, coord, player_num))


def IsPuttableCoordExist(raw_field: np.ndarray, player_num: int) -> bool:
    for col in range(raw_field.shape[0]):
        for row in range(raw_field.shape[1]):
            if IsCoordValid(raw_field, np.array([col, row]), player_num):
                return True
    return False


def GetCoordNum(field_size: np.ndarray, coord: np.ndarray) -> np.ndarray:
    coord = coord.astype('int')
    coord_num = np.zeros(field_size)
    coord_num[coord[0], coord[1]] = 1
    coord_num = coord_num.reshape([-1])
    return coord_num


def GetField3dimOnehot(field: np.ndarray) -> np.ndarray:
    field3 = np.zeros([field.shape[0], field.shape[1], 3])

    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            field3[col, row, GetValue(field, np.array([col, row])) + 1] = 1

    return field3


def RestoreField(field: np.ndarray) -> np.ndarray:
    field2 = np.zeros([field.shape[0], field.shape[1]])

    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            if field[col, row, 1] == 1:
                field2[col, row] = 0
            elif field[col, row, 2] == 1:
                field2[col, row] = 1
            else:
                field2[col, row] = -1

    return field2


def GetTestCoord(field: np.ndarray) -> np.ndarray:
    field = RestoreField(field)
    coord = np.zeros(field.shape)
    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            if IsCoordValid(field, np.array([col, row]), 1):
                coord[col, row] = 1
    coord = np.reshape(coord, [-1])
    return coord


def ReversePlayernumField(field: np.ndarray) -> np.ndarray:
    field = np.empty(field.shape)
    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            field[col, row] = GetNextPlayer(field[col, row])
    return field
