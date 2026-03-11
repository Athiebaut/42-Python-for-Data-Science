from ft_filter import ft_filter


def main():
    """Compare ft_filter with built-in filter on a few useful cases."""
    truthy_items = [0, 1, "", "ok", [], [1], False, True]
    words = "Hello the World from Python".split()

    def predicate(word):
        return len(word) > 4

    print(list(ft_filter(None, truthy_items)))
    print(list(filter(None, truthy_items)))
    print(list(ft_filter(predicate, words)))
    print(list(filter(predicate, words)))
    print(list(ft_filter(lambda n: n % 2 == 0, (n for n in range(6)))))


if __name__ == "__main__":
    main()
