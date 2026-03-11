from NULL_not_found import NULL_not_found


def main():
    """Run the subject cases, then a few values that should fail."""
    nothing = None
    garlic = float("NaN")
    zero = 0
    empty = ""
    fake = False

    NULL_not_found(nothing)
    NULL_not_found(garlic)
    NULL_not_found(zero)
    NULL_not_found(empty)
    NULL_not_found(fake)
    print(NULL_not_found("Brian"))

    print("\nExtra checks:")
    for value in (True, [], "0", {}):
        print(NULL_not_found(value))


if __name__ == "__main__":
    main()
