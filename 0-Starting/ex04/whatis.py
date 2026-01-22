import sys


def is_even(number: int) -> str:
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


def main():
    try:
        if len(sys.argv) == 1:
            return
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")

        number = int(sys.argv[1])
        print(is_even(number))
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
