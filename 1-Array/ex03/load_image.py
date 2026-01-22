import cv2

import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image and return its pixels as a NumPy array in RGB order.

    Prints the image shape using the format expected by the subject:
    "The shape of image is: (H, W, C)".
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        image = cv2.imread(path)
        if image is None:
            raise ValueError(f"unable to load image: {path}")

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"The shape of image is: {image.shape}")
        return image
    except Exception as exc:
        print(f"Error: {exc}")
        return None
