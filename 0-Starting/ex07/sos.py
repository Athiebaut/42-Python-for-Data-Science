import sys


def ft_translate(txt: str) -> dict:
    """
    Translate a text string into Morse code.

    Each character of the input string is converted into its corresponding
    Morse code representation. Characters are separated by spaces.

    Args:
        txt (str): The text to translate (expected to be uppercase).

    Returns:
        str: A string containing the Morse code translation.

    Raises:
        AssertionError: If the text contains a character not supported
                        by the Morse dictionary.
    """
    result = ""
    myDict = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-'
    }
    for kitten in txt:
        if kitten in myDict:
            result += myDict[kitten] + ' '
        else:
            raise AssertionError("bad character")
    return result.strip()


def main():
    """
    Main entry point of the program.

    Expects exactly one command-line argument, translates it into Morse code,
    and prints the result.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("bad arguments")
        if not isinstance(sys.argv[1], str):
            raise AssertionError("this is not a string")

        txt = sys.argv[1]
        result = ft_translate(txt.upper())
        print(f"{result}")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
