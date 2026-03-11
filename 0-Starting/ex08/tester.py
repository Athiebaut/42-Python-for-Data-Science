from time import sleep
from Loading import ft_tqdm

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    tqdm = None


def main():
    """Exercise ft_tqdm on short and long ranges, compare if tqdm exists."""
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in ft_tqdm(range(5)):
        sleep(0.01)
    print()

    if tqdm is not None:
        for elem in tqdm(range(333)):
            sleep(0.005)
        print()


if __name__ == "__main__":
    main()
