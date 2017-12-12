import os
import json
import numpy as np

config = json.load(open("config.json", "r"))

fields = np.load(config["datasets_x_path"])  # type: np.ndarray
coords = np.load(config["datasets_y_path"])  # type: np.ndarray

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
        print(fields[int(str), :])
    elif str == "1":
        print("Coord")
        print("num:0-", end="")
        print(coords.shape[0], end="")
        print(" > ", end="")
        str = input()
        print(coords[int(str):])
