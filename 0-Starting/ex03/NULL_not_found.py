def NULL_not_found(object: any) -> int:
    """Print the matching null-like type and return its status code."""
    if object is None:
        type_name = "Nothing"
    elif isinstance(object, float) and object != object:
        type_name = "Cheese"
    elif (
        isinstance(object, int)
        and not isinstance(object, bool)
        and object == 0
    ):
        type_name = "Zero"
    elif isinstance(object, str) and object == "":
        type_name = "Empty"
    elif object is False:
        type_name = "Fake"
    else:
        print("Type not Found")
        return 1

    if type_name == "Empty":
        print(f"{type_name}: {type(object)}")
    else:
        print(f"{type_name}: {object} {type(object)}")
    return 0
