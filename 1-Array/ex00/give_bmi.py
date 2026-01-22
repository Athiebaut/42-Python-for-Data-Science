
def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for multiple individuals.

    The BMI is computed using the formula:
        BMI = w / (h * h)

    Args:
        h (list[int | float]): A list of hs (in meters).
        w (list[int | float]): A list of ws (in kilograms).

    Returns:
        list[int | float]: A list containing BMI values for each individual.
                           Returns an empty list if an error occurs.
    """
    try:
        if len(h) != len(w):
            raise ValueError("Lists of hs and ws must have the same lengh")
        values = []
        for h, w in zip(h, w):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise ValueError("h's or w's must be int or float")
            if h <= 0 or w <= 0:
                raise ValueError("h's or w's value must be at least positive")
            bmi = w / (h * h)
            values.append(bmi)
        return values
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values against a given limit.

    For each BMI value, the function determines whether it exceeds
    the specified limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The limit to compare against.

    Returns:
        list[bool]: A list of boolean values indicating whether each BMI
                    value is greater than the given limit.
                    Returns an empty list if an error occurs.
    """
    try:
        if not isinstance(limit, (int, float)):
            raise ValueError("Limit and BMI must be int or float")
        is_limit = []
        for elm in bmi:
            if not isinstance(elm, (int, float)):
                raise ValueError("Elements of BMI must be int or float")
            is_limit.append(elm > limit)
        return is_limit
    except Exception as e:
        print(f"Error: {e}")
        return []
