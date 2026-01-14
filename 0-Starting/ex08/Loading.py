import sys

def ft_tqdm(lst: range) -> Iterator[...]:
    total = len(lst)
    width = 42
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        filled_length = int(width * progress)
    sys.stdout.write('\n')