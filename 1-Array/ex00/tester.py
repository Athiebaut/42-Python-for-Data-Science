from give_bmi import apply_limit, give_bmi


def main():
    """Run the subject test case for give_bmi and apply_limit."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
