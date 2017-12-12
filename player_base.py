import numpy as np


class PlayerBase:
    __player_num = -1  # type: int
    __player_name = ""  # type: str
    __field_size = np.empty(2)  # type: np.ndarray

    def execute_(self, raw_field: np.ndarray) -> np.ndarray:
        return np.array([-1, -1])

    def result_(self, result: bool) -> None:
        return

    def pass_(self, raw_field: np.ndarray) -> None:
        return

    def end_(self, raw_field: np.ndarray, winner: int) -> None:
        return

    def get_player_number(self) -> int:
        return self.__player_num

    def get_player_name(self) -> str:
        return self.__player_name

    def get_field_size(self) -> np.ndarray:
        return self.__field_size

    def __init__(self, player_num: int, field_size: np.array, *, player_name="Player") -> None:
        self.__player_num = player_num
        self.__player_name = player_name
        self.__field_size = field_size