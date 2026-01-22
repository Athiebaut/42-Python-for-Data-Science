
def all_thing_is_obj(object: any) -> int:

    t_object = type(object)

    if isinstance(object, list):
        print(f"List : {t_object}")
    elif isinstance(object, tuple):
        print(f"Tuple : {t_object}")
    elif isinstance(object, set):
        print(f"Set : {t_object}")
    elif isinstance(object, dict):
        print(f"Dict : {t_object}")
    elif isinstance(object, str):
        if (object == "Brian"):
            print(f"Brian is in the kitchen : {t_object}")
        elif (object == "Toto"):
            print(f"Toto is in the kitchen : {t_object}")
        else:
            print(f"Str : {t_object}")
    elif isinstance(object, int):
        print("Type not found")
    else:
        print("Type not found")
    return 42
