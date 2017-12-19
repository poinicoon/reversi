import numpy as np

from funcs import IsCoordInRange, IsEmptyCoordExist, IsCoordValid, IsPuttableCoordExist, GetNumOfPlayerPosition, \
    GetMostPlayerNumber, GetGettablePositionList, GetNumOfGettablePosition, GetCenterCoord, GetNextPlayer


class Field:
    __field = None  # type: np.ndarray

    def __set_value(self, coord: np.ndarray, value: int) -> None:
        coord = coord.astype('int')
        self.__field[coord[0], coord[1]] = value

    def get_field_size(self) -> np.ndarray:
        return np.array(self.__field.shape)

    def get_value(self, coord: np.ndarray) -> int:
        coord = coord.astype('int')
        return self.__field[coord[0], coord[1]]

    def is_coord_in_range(self, coord: np.ndarray) -> bool:
        return IsCoordInRange(self.__field, coord)

    def is_empty_coord_exist(self) -> bool:
        return IsEmptyCoordExist(self.__field)

    def is_coord_valid(self, coord: np.ndarray, player_num: int) -> bool:
        return IsCoordValid(self.__field, coord, player_num)

    def is_puttable_coord_exist(self, player_num: int) -> bool:
        return IsPuttableCoordExist(self.__field, player_num)

    def get_num_of_player_position(self, player_num: int) -> int:
        return GetNumOfPlayerPosition(self.__field, player_num)

    def get_most_player_number(self) -> int:
        return GetMostPlayerNumber(self.__field)

    def get_gettable_position_list(self, coord: np.ndarray, player_num: int) -> [np.ndarray]:
        return GetGettablePositionList(self.__field, coord, player_num)

    def get_num_of_gettable_position(self, coord: np.ndarray, player_num: int) -> int:
        return GetNumOfGettablePosition(self.__field, coord, player_num)

    def get_field(self) -> np.ndarray:
        return self.__field

    def put(self, coord: np.ndarray, player_num: int) -> bool:
        if self.is_coord_valid(coord, player_num):
            put_coord_list = self.get_gettable_position_list(coord, player_num)  # type: [np.ndarray]
            for i in range(len(put_coord_list)):
                self.__set_value(put_coord_list[i], player_num)
            return True
        else:
            return False

    def __init__(self, field_size: np.ndarray) -> None:
        ul = GetCenterCoord(field_size, 0)  # type: np.ndarray
        ur = GetCenterCoord(field_size, 1)  # type: np.ndarray
        dl = GetCenterCoord(field_size, 2)  # type: np.ndarray
        dr = GetCenterCoord(field_size, 3)  # type: np.ndarray

        self.__field = np.empty(field_size)
        self.__field.fill(-1)

        self.__set_value(ul, np.random.randint(2))
        self.__set_value(ur, GetNextPlayer(self.get_value(ul)))
        self.__set_value(dl, self.get_value(ur))
        self.__set_value(dr, self.get_value(ul))
