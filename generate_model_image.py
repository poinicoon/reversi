"""
モデルからモデル画像を生成する。
"""

import sys
from keras.models import load_model
from keras.utils import plot_model


def main(model_path, model_image_path):
    model = load_model(model_path)
    plot_model(model, to_file=model_image_path, show_shapes=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
