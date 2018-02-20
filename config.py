from pathlib import Path

ProjectName = "reversi_nn"

WORK_DIR = Path.home().joinpath("." + ProjectName)

MODEL_PATH = WORK_DIR.joinpath("model.h5")
MODEL_IMAGE_PATH = WORK_DIR.joinpath("model.png")

X_TRAIN_PATH = WORK_DIR.joinpath("x_train.npy")
Y_TRAIN_PATH = WORK_DIR.joinpath("y_train.npy")
X_TEST_PATH = WORK_DIR.joinpath("x_test.npy")
Y_TEST_PATH = WORK_DIR.joinpath("y_test.npy")
