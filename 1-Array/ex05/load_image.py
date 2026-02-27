import os

import cv2
import numpy as np


def resolve_image_path(path: str) -> str:
    """
    Resolve image path for local runs and fallback to ex02 assets.
    """
    if os.path.isfile(path):
        return path

    base_dir = os.path.dirname(__file__)
    local_candidate = os.path.join(base_dir, path)
    if os.path.isfile(local_candidate):
        return local_candidate

    fallback_candidate = os.path.join(
        base_dir, "..", "ex02", os.path.basename(path)
    )
    if os.path.isfile(fallback_candidate):
        return fallback_candidate

    return path


def ft_load(path: str) -> np.ndarray | None:
    """
    Load a JPG/JPEG image and return its pixels in RGB format.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        real_path = resolve_image_path(path)
        ext = os.path.splitext(real_path)[1].lower()
        if ext not in {".jpg", ".jpeg"}:
            raise ValueError("only .jpg and .jpeg files are supported")

        image = cv2.imread(real_path)
        if image is None:
            raise ValueError(f"unable to load image: {path}")

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"The shape of image is: {image.shape}")
        print(image)
        return image
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def main() -> None:
    """
    Basic manual test entrypoint for ft_load.
    """
    try:
        ft_load("landscape.jpg")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
