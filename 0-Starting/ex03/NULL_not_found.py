def NULL_not_found(object: any) -> int:

    if object is None:
        type_name = "Nothing"
    elif isinstance(object, float) and object != object:
        type_name = "Cheese"
    elif isinstance(object, bool):
        type_name = "Fake"
    elif object == 0:
        type_name = "Zero"
    elif object == '':
        type_name = "Empty"
    else:
        print("Type not Found")
        return 1
    if type_name == "Empty":
        print(f"{type_name}: {type(object)}")
    else:
        print(f"{type_name}: {object} {type(object)}")
    return 0