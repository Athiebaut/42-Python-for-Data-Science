def count_in_list(lst, word) -> int:
    """Count the occurrences of `word` in `lst`."""
    return sum(1 for item in lst if item == word)
