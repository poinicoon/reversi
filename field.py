import numpy as np

import funcs


class Field:
    __raw_field = None  # type: np.ndarray

    def __set_value(self, coord: np.ndarray, value: int) -> None:
        self.__raw_field[coord[0], coord[1]] = value

    def get_field_size(self) -> np.ndarray:
        return np.array(self.__raw_field.shape)

    def get_value(self, coord: np.ndarray) -> int:
        return self.__raw_field[coord[0], coord[1]]

    def is_coord_in_range(self, coord: np.ndarray) -> bool:
        return funcs.is_coord_in_range(self.__raw_field, coord)

    def is_empty_coord_exist(self) -> bool:
        return funcs.is_empty_coord_exist(self.__raw_field)

    def is_coord_valid(self, coord: np.ndarray, player_num: int) -> bool:
        return funcs.is_coord_valid(self.__raw_field, coord, player_num)

    def is_puttable_coord_exist(self, player_num: int) -> bool:
        return funcs.is_puttable_coord_exist(self.__raw_field, player_num)

    def get_num_of_player_position(self, player_num: int) -> int:
        return funcs.get_num_of_player_position(self.__raw_field, player_num)

    def get_most_player_number(self) -> int:
        return funcs.get_most_player_number(self.__raw_field)

    def get_gettable_position_list(self, coord: np.ndarray, player_num: int) -> [np.ndarray]:
        return funcs.get_gettable_position_list(self.__raw_field, coord, player_num)

    def get_num_of_gettable_position(self, coord: np.ndarray, player_num: int) -> int:
        return funcs.get_num_of_gettable_position(self.__raw_field, coord, player_num)

    def get_corner_coord(self, corner_num: int) -> np.ndarray:
        return funcs.get_corner_coord(self.get_field_size(), corner_num)

    def get_center_coord(self, center_num: int) -> np.ndarray:
        return funcs.get_center_coord(self.get_field_size(), center_num)

    def get_raw_field(self) -> np.ndarray:
        return np.array(self.__raw_field)

    def put(self, coord: np.ndarray, player_num: int) -> bool:
        if self.is_coord_valid(coord, player_num):
            put_coord_list = self.get_gettable_position_list(coord, player_num)  # type: [np.ndarray]
            for i in range(len(put_coord_list)):
                self.__set_value(put_coord_list[i], player_num)
            return True
        else:
            return False

    def __init__(self, field_size: np.ndarray) -> None:
        ul = funcs.get_center_coord(field_size, 0)  # type: np.ndarray
        ur = funcs.get_center_coord(field_size, 1)  # type: np.ndarray
        dl = funcs.get_center_coord(field_size, 2)  # type: np.ndarray
        dr = funcs.get_center_coord(field_size, 3)  # type: np.ndarray

        self.__raw_field = np.empty(field_size, dtype="int32")
        self.__raw_field.fill(-1)

        self.__set_value(ul, funcs.generate_random(0, 2))
        self.__set_value(ur, funcs.get_next_player(self.get_value(ul)))
        self.__set_value(dl, self.get_value(ur))
        self.__set_value(dr, self.get_value(ul))
