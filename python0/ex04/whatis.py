import sys

try:
    if len(sys.argv) > 2:
        raise Exception("AssertionError: more than one argument is provided")
    num = int(sys.argv[1])
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer", file=sys.stderr)
except IndexError:
    pass
except Exception as e:
    print(e, file=sys.stderr)
