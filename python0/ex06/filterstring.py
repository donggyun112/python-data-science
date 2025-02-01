from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise Exception()
        string = str(sys.argv[1])
        if not string:
            raise Exception()
        number = int(sys.argv[2])

        words = string.split(" ")
        print(list(ft_filter(lambda x: len(x) > number, words)))
    except Exception:
        print("AssertionError: the arguments are bad", file=sys.stderr)


if __name__ == "__main__":
    main()
