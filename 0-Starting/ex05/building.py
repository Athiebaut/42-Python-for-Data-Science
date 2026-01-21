import sys

def count_chars(txt: str) -> list:
    """
    Count different types of characters in a string.

    The function counts:
    - uppercase letters
    - lowercase letters
    - punctuation marks (, . ! ?)
    - spaces and newline characters
    - digits

    Args:
        txt (str): The input text to analyze.

    Returns:
        list: A list of integers containing:
              [uppercase, lowercase, punctuation, spaces, digits, total]
    """
    array = [0, 0, 0, 0, 0, 0]
    for kitten in txt:
        if kitten.isupper():
            array[0] += 1
        elif kitten.islower():
            array[1] += 1
        elif kitten == ',' or kitten == '.' or kitten == '!' or kitten == '?':
            array[2] += 1
        elif kitten == ' ' or kitten == '\n':
            array[3] += 1
        elif kitten.isdigit():
            array[4] += 1
    array[5] = array[0] + array[1] + array[2] + array[3] + array[4]
    return array


def main():
    """
    Main entry point of the program.

    Reads text either from standard input or from a command-line argument,
    then displays statistics about the characters contained in the text.
    """
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            txt = sys.stdin.read()
        elif len(sys.argv) == 2:
            txt = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        infos = count_chars(txt)
        print(f"The text contains {infos[5]} characters:")
        print(f"{infos[0]} upper letters")
        print(f"{infos[1]} lower letters")
        print(f"{infos[2]} ponctuation marks")
        print(f"{infos[3]} spaces")
        print(f"{infos[4]} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()

