

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("Lists of heights and weights must have the same lengh")
        values = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise ValueError("Height's or weight's must be int or float")
            if h <= 0 or w <= 0:
                raise ValueError("Height's or weight's value must be at least positive")
            bmi = w / (h * h) 
            values.append(bmi)
        return (values)
    except Exception as e:
        print(f"An error as occured : " + {e})
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not isinstance(limit, (int, float)):
            raise ValueError("Limit and BMI must be int or float")
        is_limit = []
        for l in bmi:
            if not isinstance(l, (int, float)):
                raise ValueError("Elements of BMI must be int or float")
            is_limit.append(l > limit)
        return is_limit
    except Exception as e:
        print(f"An error as occured : " + {e})
        return []