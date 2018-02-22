import sys
from keras.models import load_model
from keras.utils import plot_model

if __name__ == "__main__":
    model_path = sys.argv[1]
    model_image_path = sys.argv[2]

    model = load_model(model_path)

    plot_model(model, to_file=model_image_path, show_shapes=True)
