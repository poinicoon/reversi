import os
import numpy as np

work_dir = os.environ["HOME"] + os.sep + "reversi_learn"

filename_fields = work_dir + os.sep + "datasets_x.npy"
filename_coords = work_dir + os.sep + "datasets_y.npy"

fields = np.load(filename_fields)  # type: np.ndarray
coords = np.load(filename_coords)  # type: np.ndarray

str = ""
while str != "exit":
    print("Field:0, Coord:1 > ", end="")
    str = input()
    if str == "0":
        print("Field")
        print("num:0-", end="")
        print(fields.shape[0], end="")
        print(" > ", end="")
        str = input()
        print(fields[int(str),:])
    elif str == "1":
        print("Coord")
        print("num:0-", end="")
        print(coords.shape[0], end="")
        print(" > ", end="")
        str = input()
        print(coords[int(str):])
