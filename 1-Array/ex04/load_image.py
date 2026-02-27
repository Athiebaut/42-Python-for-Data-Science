import os

import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Load a JPG/JPEG image and return its pixels in RGB format.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        ext = os.path.splitext(path)[1].lower()
        if ext not in {".jpg", ".jpeg"}:
            raise ValueError("only .jpg and .jpeg files are supported")

        image = cv2.imread(path)
        if image is None:
            raise ValueError(f"unable to load image: {path}")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def main() -> None:
    """
    Basic manual test entrypoint for ft_load.
    """
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        print(f"The shape of image is: {image.shape}")
        print(image)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
