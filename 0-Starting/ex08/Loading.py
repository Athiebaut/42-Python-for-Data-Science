import os


def ft_tqdm(lst: range) -> None:
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
    if total == 0:
        return
    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80
    total_str = str(total)
    bar_width = max(10, term_width - len(f"100%|[]| {total_str}/{total_str}"))

    for i, item in enumerate(lst):
        current = i + 1
        progress = current / total
        filled = int(bar_width * progress)
        if filled >= bar_width:
            bar = "=" * (bar_width - 1) + ">"
        else:
            bar = "=" * filled + ">" + " " * (bar_width - filled - 1)
        print(
            f"\r{int(progress * 100):3d}%|[{bar}]| {current}/{total}",
            end="",
            flush=True,
        )
        yield item
    print()
