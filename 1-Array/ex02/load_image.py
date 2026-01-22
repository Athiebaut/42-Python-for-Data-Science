import cv2
import array


def ft_load(path: str) -> array:
    """
    Load an image from disk and return its pixels in RGB format.

    Prints the shape of the image.
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
    except Exception as e:
        print(f"Error: {e}")
        return None
