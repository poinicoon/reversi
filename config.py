import os
from pathlib import Path

WorkDir = Path.home().joinpath(".reversi_nn")
ModelPath = WorkDir.joinpath("model.h5")
ModelImagePath = WorkDir.joinpath("model.png")
XTrainPath = WorkDir.joinpath("x_train.npy")
YTrainPath = WorkDir.joinpath("y_train.npy")
XTestPath = WorkDir.joinpath("x_test.npy")
YTestPath = WorkDir.joinpath("y_test.npy")