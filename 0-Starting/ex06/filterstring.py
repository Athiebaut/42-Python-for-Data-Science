import sys
from ft_filter import ft_filter


def main():
    """
    Main entry point of the program.

    Expects two command-line arguments:
    - a string containing words
    - an integer used as a length threshold

    The program filters and prints all words whose length
    is strictly greater than the given integer.
    """
    try:
        if len(sys.argv) == 3:
            txt = sys.argv[1]
            nbr = int(sys.argv[2])
            result = ft_filter(lambda x: len(x) > nbr, txt.split())
            print(f"{result}")
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
