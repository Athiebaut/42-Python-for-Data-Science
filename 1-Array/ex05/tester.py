import os

from load_image import ft_load
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey
from pimp_image import ft_invert
from pimp_image import ft_red


def main():
    """Run the subject test case for image filters."""
    image_path = os.path.join(os.path.dirname(__file__), "landscape.jpg")
    array = ft_load(image_path)
    if array is None:
        return
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
