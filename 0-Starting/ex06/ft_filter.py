
def ft_filter(function, iterable):
    """
    Apply a function to filter elements from an iterable.

    Args:
        function (callable): A function that takes one argument and returns True
                             if the element should be kept.
        iterable (iterable): An iterable containing elements to filter.

    Returns:
        list: A list containing elements for which function(item) is True.
    """
    return [item for item in iterable if function(item)]
