import random
import numpy as np
import matplotlib.pyplot as plt


def generate_random(begin: int, end: int) -> int:
    return round(random.uniform(begin, end - 1))


def get_next_player(player_num: int) -> int:
    if player_num == 0:
        return 1
    elif player_num == 1:
        return 0
    else:
        return -1


def get_corner_coord(field_size: np.ndarray, corner_num: int) -> np.ndarray:
    if corner_num == 0:
        return np.array([0, 0], dtype="int32")
    elif corner_num == 1:
        return np.array([0, int(field_size[1] - 1)], dtype="int32")
    elif corner_num == 2:
        return np.array([int(field_size[0]) - 1, 0], dtype="int32")
    elif corner_num == 3:
        return np.array([int(field_size[0]) - 1, int(field_size[1]) - 1], dtype="int32")
    else:
        return np.array([-1, -1], dtype="int32")


def get_center_coord(field_size: np.ndarray, center_num: int) -> np.ndarray:
    if center_num == 0:
        return np.array([field_size[0] / 2 - 1, field_size[1] / 2 - 1], dtype="int32")
    elif center_num == 1:
        return np.array([field_size[0] / 2 - 1, field_size[1] / 2], dtype="int32")
    elif center_num == 2:
        return np.array([field_size[0] / 2, field_size[1] / 2 - 1], dtype="int32")
    elif center_num == 3:
        return np.array([field_size[0] / 2, field_size[1] / 2], dtype="int32")
    else:
        return np.array([-1, -1], dtype="int32")


def get_vector(direc_num: int, move_size: int) -> np.ndarray:
    if direc_num == 0:
        return np.array([-move_size, -move_size], dtype="int32")
    elif direc_num == 1:
        return np.array([-move_size, 0], dtype="int32")
    elif direc_num == 2:
        return np.array([-move_size, move_size], dtype="int32")
    elif direc_num == 3:
        return np.array([0, -move_size], dtype="int32")
    elif direc_num == 4:
        return np.array([0, move_size], dtype="int32")
    elif direc_num == 5:
        return np.array([move_size, -move_size], dtype="int32")
    elif direc_num == 6:
        return np.array([move_size, 0], dtype="int32")
    elif direc_num == 7:
        return np.array([move_size, move_size], dtype="int32")
    else:
        return np.array([0, 0], dtype="int32")


def get_moved_coord(coord: np.ndarray, direc_num: int, move_size: int) -> np.ndarray:
    return coord + get_vector(direc_num, move_size)


def is_coord_in_range(raw_field: np.ndarray, coord: np.ndarray) -> bool:
    return bool(-1 < coord[0] < raw_field.shape[0] and -1 < coord[1] < raw_field.shape[1])


def get_num_of_player_position(raw_field: np.ndarray, player_num: int) -> int:
    sum = 0  # type: int
    for col in range(raw_field.shape[0]):
        for row in range(raw_field.shape[1]):
            if raw_field[col, row] == player_num:
                sum += 1
    return sum


def is_empty_coord_exist(raw_field: np.ndarray) -> bool:
    return bool(0 < get_num_of_player_position(raw_field, -1))


def get_most_player_number(raw_field: np.ndarray) -> int:
    num_of_pos = (
        get_num_of_player_position(raw_field, 0),
        get_num_of_player_position(raw_field, 1)
    )  # type: (int, int)

    if num_of_pos[1] < num_of_pos[0]:
        return 0
    elif num_of_pos[0] < num_of_pos[1]:
        return 1
    else:
        return 2


def get_gettable_position_list(raw_field: np.ndarray, put_coord: np.ndarray, player_num: int) -> [np.ndarray]:
    next_player_num = get_next_player(player_num)
    field_max = max(raw_field.shape)  # type: int
    gettable_pos_list = []  # type: [np.ndarray]

    # coord is not empty
    if raw_field[put_coord[0], put_coord[1]] != -1:
        return gettable_pos_list

    # coord is out of field
    if not (is_coord_in_range(raw_field, put_coord)):
        return gettable_pos_list

    for direc_num in range(8):
        tmp_coord = get_moved_coord(put_coord, direc_num, 1)  # type: np.ndarray
        if not (is_coord_in_range(raw_field, tmp_coord)):
            continue

        # next position is not next player
        tmp_coord = get_moved_coord(put_coord, direc_num, 1)
        if raw_field[tmp_coord[0], tmp_coord[1]] != next_player_num:
            continue

        for move_size in range(2, field_max):
            tmp_coord = get_moved_coord(put_coord, direc_num, move_size)  # type: np.ndarray

            if not (is_coord_in_range(raw_field, tmp_coord)):
                break

            if raw_field[tmp_coord[0], tmp_coord[1]] == next_player_num:
                continue

            if raw_field[tmp_coord[0], tmp_coord[1]] == player_num:
                if len(gettable_pos_list) == 0:
                    gettable_pos_list.append(put_coord)

                for move_size2 in range(1, move_size + 1):
                    tmp_coord = get_moved_coord(put_coord, direc_num, move_size2)
                    gettable_pos_list.append(tmp_coord)

                break

            if raw_field[tmp_coord[0], tmp_coord[1]] == -1:
                break

    return gettable_pos_list


def get_num_of_gettable_position(raw_field: np.ndarray, coord: np.ndarray, player_num: int) -> int:
    return len(get_gettable_position_list(raw_field, coord, player_num))


def is_coord_valid(raw_field: np.ndarray, coord: np.ndarray, player_num: int) -> bool:
    return bool(0 < get_num_of_gettable_position(raw_field, coord, player_num))


def is_puttable_coord_exist(raw_field: np.ndarray, player_num: int) -> bool:
    for col in range(raw_field.shape[0]):
        for row in range(raw_field.shape[1]):
            if is_coord_valid(raw_field, np.array([col, row]), player_num):
                return True
    return False


def normalize_min_max(value: int, min: int, max: int):
    return int((value - min) / (max - min))


def normalize_field(raw_field: np.ndarray) -> np.ndarray:
    return (raw_field + 1) / 2


def coord_to_num(field_size: np.ndarray, coord: np.ndarray) -> int:
    return coord[0] * field_size[1] + coord[1]

def coord_to_3dim(field_size, coord, player_num):
    tmp_coord = np.zeros([3, field_size[0], field_size[1]])
    tmp_coord[player_num + 1, coord[0], coord[1]] = 1

    return tmp_coord



def num_to_coord(num: int, field_size: np.ndarray) -> np.ndarray:
    field = np.array(range(field_size[0] * field_size[1])).reshape(field_size)
    for col in range(field_size[0]):
        for row in range(field_size[1]):
            if field[col, row] == num:
                return np.array([col, row])
    return np.array([-1, -1])


def field_ndim_2_to_3(field: np.ndarray) -> np.ndarray:
    field3 = np.zeros([3, field.shape[0], field.shape[1]])

    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            if field[col, row] == 0:
                field3[1, col, row] = 1
            elif field[col, row] == 1:
                field3[2, col, row] = 1
            else:
                field3[0, col, row] = 1

    return field3


def reverse_playernum_field(field: np.ndarray) -> np.ndarray:
    field = np.empty(field.shape)
    for col in range(field.shape[0]):
        for row in range(field.shape[1]):
            field[col, row] = get_next_player(field[col, row])
    return field


def draw_field(field: np.ndarray):
    plt.imshow(field, cmap='gray', interpolation='none')
    plt.show()


def print_field(raw_field: np.ndarray) -> None:
    print("Field")
    for col in range(raw_field.shape[0]):
        for row in range(raw_field.shape[1]):
            if raw_field[col, row] == -1:
                print(".", end=" ")
            else:
                print(raw_field[col, row], end=" ")
        print()
