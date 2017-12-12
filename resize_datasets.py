import numpy as np

filename_fields = "datasets/fields.npy"
filename_coords = "datasets/coords.npy"

num = 5000

fields = np.load(filename_fields)  # type: np.ndarray
coords = np.load(filename_coords)  # type: np.ndarray

fields = np.resize(fields, [num, fields.shape[1], fields.shape[2]])
coords = np.resize(coords, [num, coords.shape[1]])

print("Resized ", end="")
print(fields.shape)

np.save(filename_fields, fields)
np.save(filename_coords, coords)

print("Saved")