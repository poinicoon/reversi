import json
import numpy as np

config = json.load(open("config.json", "r"))

print("x_train: ", end="")
print(np.load(config["x_train_path"]).shape)

print("y_train: ", end="")
print(np.load(config["y_train_path"]).shape)

print("x_test: ", end="")
print(np.load(config["x_test_path"]).shape)

print("y_test: ", end="")
print(np.load(config["y_test_path"]).shape)
