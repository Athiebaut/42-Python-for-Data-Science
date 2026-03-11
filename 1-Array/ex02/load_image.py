import os

import cv2
import numpy as np


def resolve_image_path(path: str) -> str:
    """Resolve an image path from the exercise directory when needed."""
    if os.path.isabs(path) or os.path.isfile(path):
        return path
    return os.path.join(os.path.dirname(__file__), path)


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image from disk and return its pixels in RGB format.

    Prints the shape of the image.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        real_path = resolve_image_path(path)
        if not os.path.isfile(real_path):
            raise ValueError(f"unable to load image: {path}")

        image = cv2.imread(real_path)
        if image is None:
            raise ValueError(f"unable to load image: {path}")

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"The shape of image is: {image.shape}")
        return image
    except Exception as e:
        print(f"Error: {e}")
        return None
