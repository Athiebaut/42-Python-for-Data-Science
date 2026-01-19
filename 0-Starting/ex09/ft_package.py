def count_in_list(lst: range, word):
    count = 0
    for item in lst:
        if item == word:
            count += 1
    return count
