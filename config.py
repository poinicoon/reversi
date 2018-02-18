from pathlib import Path

ProjectName = "reversi_nn"

WorkDir = Path.home().joinpath("." + ProjectName)

ModelPath = WorkDir.joinpath("model.h5")
ModelImagePath = WorkDir.joinpath("model.png")
XTrainPath = WorkDir.joinpath("x_train.npy")
YTrainPath = WorkDir.joinpath("y_train.npy")
XTestPath = WorkDir.joinpath("x_test.npy")
YTestPath = WorkDir.joinpath("y_test.npy")
