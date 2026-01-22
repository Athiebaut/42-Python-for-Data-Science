import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array (list of lists) between start and end.

    Prints the original and sliced shapes, then returns the sliced data
    as a standard Python list (list of lists).
    """
    try:
        if not isinstance(family, list) or not family:
            raise TypeError("family must be a non-empty list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integers")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("family must be a 2D list (list of lists)")

        row_len = len(family[0])
        if row_len == 0 or any(len(row) != row_len for row in family):
            raise ValueError("all rows must have the same non-zero length")

        array = np.array(family)
        print("My shape is :", array.shape)
        sliced = array[start:end]
        print("My new shape is :", sliced.shape)
        return sliced.tolist()
    except Exception as exc:
        print(f"Error: {exc}")
        return []
