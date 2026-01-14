import sys

def ft_translate(txt : str) -> dict:
    result = ""
    myDict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-'}   
    for kitten in txt:
        if kitten in myDict:
            result += myDict[kitten] + ' '
        else:
            raise AssertionError("bad character")
    return result.strip()

def main():
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