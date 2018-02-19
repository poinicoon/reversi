from pathlib import Path

ProjectName = "reversi_nn"

DIR_CONFIG = Path.home().joinpath("." + ProjectName)

PATH_MODEL = DIR_CONFIG.joinpath("model.h5")
PATH_MODELIMAGE = DIR_CONFIG.joinpath("model.png")

PATH_XTRAIN = DIR_CONFIG.joinpath("x_train.npy")
PATH_YTRAIN = DIR_CONFIG.joinpath("y_train.npy")
PATH_XTEST = DIR_CONFIG.joinpath("x_test.npy")
PATH_YTEST = DIR_CONFIG.joinpath("y_test.npy")
