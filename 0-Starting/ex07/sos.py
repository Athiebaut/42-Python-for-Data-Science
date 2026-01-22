import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def ft_translate(txt: str) -> str:
    """
    Translate a text string into Morse code.

    The program supports space and alphanumeric characters only.
    """
    morse = []
    for char in txt.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse.append(NESTED_MORSE[char])
    return " ".join(morse)


def main():
    """
    Main entry point of the program.

    Expects exactly one command-line argument, translates it into Morse code,
    and prints the result.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        print(ft_translate(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
