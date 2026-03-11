def all_thing_is_obj(object: any) -> int:
    """Print the object type using the format expected by the subject."""
    object_type = type(object)

    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type not found")
    return 42
