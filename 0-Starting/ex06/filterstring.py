import sys
from ft_filter import ft_filter

def main():
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

