import sys
import os

def ft_tqdm(lst: range):
    """
    Display a progress bar while iterating over a range.

    This generator yields each element of the given range while
    displaying a progress bar in the terminal, similar to tqdm.

    Args:
        lst (range): A range object to iterate over.

    Yields:
        int: The current element from the range.
    """
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = max(10, term_width - 40)

    for i, item in enumerate(lst):
        progress = (i + 1) / total
        filled = int(bar_width * progress)
        bar = '█' * filled + '░' * (bar_width - filled)
        sys.stdout.write(f'\r{int(progress * 100):3d}%|{bar}| {i + 1}/{total}')
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')

