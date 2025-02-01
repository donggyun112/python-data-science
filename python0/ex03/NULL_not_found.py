def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif object != object:
        print("Cheese: nan", type(object))
        return 0
    elif object == 0:
        print("Zero: 0", type(object))
        return 0
    elif object == "":
        print("Empty:", type(object))
        return 0
    elif object is False:
        print("Fake:", type(object))
        return 0
    else:
        print("Type not Found")
    return 1


""" $>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$> """
