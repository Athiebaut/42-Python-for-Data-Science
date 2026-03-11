import os

from load_image import ft_load


def main():
    """Run the subject test case for ft_load."""
    image_path = os.path.join(os.path.dirname(__file__), "landscape.jpg")
    print(ft_load(image_path))


if __name__ == "__main__":
    main()
