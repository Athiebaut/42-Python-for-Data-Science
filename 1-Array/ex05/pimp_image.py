import numpy as np

from load_image import ft_load


def _validate_image(array: np.ndarray) -> None:
    """
    Validate the input image format.
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy.ndarray")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("array must have shape (H, W, 3)")


def _display_image(array: np.ndarray, title: str) -> None:
    """
    Display an image with matplotlib when available.
    """
    try:
        import matplotlib.pyplot as plt

        plt.figure(title)
        plt.imshow(array)
        plt.title(title)
        plt.axis("off")
        plt.show(block=False)
        plt.pause(0.001)
    except Exception:
        return


def ft_invert(array: np.ndarray) -> np.ndarray | None:
    """
    Invert the image colors.
    """
    try:
        _validate_image(array)
        result = 255 - array
        _display_image(result, "Invert")
        return result
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray | None:
    """
    Keep only the red channel.
    """
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 1] = result[:, :, 1] * 0
        result[:, :, 2] = result[:, :, 2] * 0
        _display_image(result, "Red")
        return result
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray | None:
    """
    Keep only the green channel.
    """
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
        result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
        _display_image(result, "Green")
        return result
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray | None:
    """
    Keep only the blue channel.
    """
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        _display_image(result, "Blue")
        return result
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray | None:
    """
    Convert the image to grey while keeping the same shape.
    """
    try:
        _validate_image(array)
        grey = np.sum(array / 3, axis=2, keepdims=True)
        grey = np.clip(grey, 0, 255).astype(np.uint8)
        result = np.repeat(grey, 3, axis=2)
        _display_image(result, "Grey")
        return result
    except Exception as exc:
        print(f"Error: {exc}")
        return None


def main() -> None:
    """
    Minimal local test for all filters.
    """
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            return
        _display_image(array, "Original")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)

        try:
            import matplotlib.pyplot as plt

            plt.show()
        except Exception:
            return
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
