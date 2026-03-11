import os
import numpy as np
from load_image import ft_load


def resolve_animal_path() -> str:
    """
    Resolve animal.jpeg for local runs.
    """
    base_dir = os.path.dirname(__file__)
    candidates = [
        os.path.join(base_dir, "animal.jpeg"),
        os.path.join(base_dir, "..", "ex03", "animal.jpeg"),
    ]
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    return candidates[0]


def crop_square_channel(image: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Crop a centered square and keep one channel.
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy.ndarray")
    if image.ndim != 3 or image.shape[2] < 1:
        raise ValueError("image must have shape (H, W, C)")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")

    height, width = image.shape[:2]
    if height < size or width < size:
        raise ValueError(
            f"image is too small to crop {size}x{size}: {image.shape}"
        )

    y_start = (height - size) // 2
    x_start = (width - size) // 2
    return image[y_start: y_start + size, x_start: x_start + size, 0:1]


def manual_transpose(image: np.ndarray) -> np.ndarray:
    """
    Transpose an image manually (without numpy transpose helpers).
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy.ndarray")

    if image.ndim == 3 and image.shape[2] == 1:
        source = image[:, :, 0]
    elif image.ndim == 2:
        source = image
    else:
        raise ValueError("image must have shape (H, W, 1) or (H, W)")

    height, width = source.shape
    transposed = np.empty((width, height), dtype=source.dtype)

    for row in range(height):
        for col in range(width):
            transposed[col, row] = source[row, col]
    return transposed


def display_images(cropped: np.ndarray, transposed: np.ndarray) -> None:
    """
    Display cropped and transposed images when matplotlib is available.
    """
    try:
        import matplotlib.pyplot as plt

        figure, axes = plt.subplots(1, 2, figsize=(10, 5))
        axes[0].imshow(cropped.squeeze(), cmap="gray")
        axes[0].set_title("Cropped")
        axes[0].set_xlabel("X")
        axes[0].set_ylabel("Y")
        axes[1].imshow(transposed, cmap="gray")
        axes[1].set_title("Transposed")
        axes[1].set_xlabel("X")
        axes[1].set_ylabel("Y")
        plt.tight_layout()
        if "agg" in plt.get_backend().lower():
            plt.close(figure)
            return
        plt.show()
    except Exception:
        return


def main() -> None:
    """
    Load image, crop a square, transpose it manually, and display the result.
    """
    try:
        image = ft_load(resolve_animal_path())
        if image is None:
            return

        cropped = crop_square_channel(image, 400)
        print(f"The shape of image is: {cropped.shape}")
        print(cropped)

        transposed = manual_transpose(cropped)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        display_images(cropped, transposed)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
