import os
import cv2
import numpy as np
from load_image import ft_load


def zoom_image(img: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Crop a square part of an RGB img and keep only 1 channel.

    Returns a NumPy array of shape (size, size, 1).
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("img must be a numpy.ndarray")
    if img.ndim != 3 or img.shape[2] < 1:
        raise ValueError("img must have a shape like (H, W, C)")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")

    height, width = img.shape[0], img.shape[1]
    if height < size or width < size:
        raise ValueError(f"img is too small to crop {size}x{size}: {img.shape}")

    y0 = (height - size) // 2
    x0 = (width - size) // 2
    crop = img[y0 : y0 + size, x0 : x0 + size]
    return crop[:, :, 0:1]


def add_axis_scale(img: np.ndarray, tick_step: int = 50) -> np.ndarray:
    """
    Create a display img with x/y axis scales drawn around it.

    This is a fallback when matplotlib isn't available.
    """
    shown = img.squeeze()
    if shown.ndim == 2:
        base = shown
        if base.dtype != np.uint8:
            base = base.astype(np.uint8)
        base_bgr = cv2.cvtColor(base, cv2.COLOR_GRAY2BGR)
    elif shown.ndim == 3 and shown.shape[2] == 3:
        base = shown
        if base.dtype != np.uint8:
            base = base.astype(np.uint8)
        base_bgr = cv2.cvtColor(base, cv2.COLOR_RGB2BGR)
    else:
        raise ValueError("unsupported img format for display")

    height, width = base_bgr.shape[:2]
    left_margin = 60
    bottom_margin = 40
    canvas = np.full((height + bottom_margin, width + left_margin, 3), 255, dtype=np.uint8)
    canvas[0:height, left_margin : left_margin + width] = base_bgr

    axis_color = (0, 0, 0)
    cv2.line(canvas, (left_margin, 0), (left_margin, height), axis_color, 1)
    cv2.line(canvas, (left_margin, height), (left_margin + width, height), axis_color, 1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    thickness = 1

    step = max(1, tick_step)
    for x in range(0, width + 1, step):
        px = left_margin + x
        cv2.line(canvas, (px, height), (px, height + 5), axis_color, 1)
        cv2.putText(
            canvas,
            str(x),
            (px - 8, height + 25),
            font,
            font_scale,
            axis_color,
            thickness,
            cv2.LINE_AA,
        )

    for y in range(0, height + 1, step):
        py = y
        cv2.line(canvas, (left_margin - 5, py), (left_margin, py), axis_color, 1)
        cv2.putText(
            canvas,
            str(y),
            (5, py + 5),
            font,
            font_scale,
            axis_color,
            thickness,
            cv2.LINE_AA,
        )

    cv2.putText(
        canvas,
        "Y",
        (5, 15),
        font,
        0.6,
        axis_color,
        1,
        cv2.LINE_AA,
    )
    cv2.putText(
        canvas,
        "X",
        (left_margin + width - 15, height + bottom_margin - 10),
        font,
        0.6,
        axis_color,
        1,
        cv2.LINE_AA,
    )
    return canvas


def display_with_scale(img: np.ndarray) -> None:
    """
    Display the img while keeping x/y axis scale visible.

    Uses matplotlib if available (recommended for this exercise).
    """
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        try:
            if not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
                return
            canvas = add_axis_scale(img)
            cv2.imshow("zoom", canvas)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as exc:
            print(f"Error: {exc}")
        return

    shown = img.squeeze()
    if shown.ndim == 2:
        plt.imshow(shown, cmap="gray")
    else:
        plt.imshow(shown)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.show()


def main() -> None:
    """
    Load "animal.jpeg", print information, crop/zoom, and display the result.
    """
    try:
        img_path = os.path.join(os.path.dirname(__file__), "animal.jpeg")
        img = ft_load(img_path)
        if img is None:
            return

        print(img)
        zoomed = zoom_img(img, 400)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        display_with_scale(zoomed)
    except Exception as exc:
        print(f"Error: {exc}")
        return


if __name__ == "__main__":
    main()
