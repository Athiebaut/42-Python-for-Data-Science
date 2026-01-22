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
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        txt = sys.argv[1]
        nbr = int(sys.argv[2])

        def predicate(word: str) -> bool:
            return len(word) > nbr

        result = [word for word in ft_filter(predicate, txt.split())]
        print(result)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
