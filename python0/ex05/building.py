import sys


def is_punctuation(char: str) -> bool:
    """ is_punctuation(char: str) -> bool \
        This function takes a character as an argument \
        and returns True if the character is a punctuation mark, \
        and False otherwise."""
    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"


def analyze_string(string: str) -> None:
    """analyze_string(string: str) -> str \n\
This function takes a string as an \
 argument and prints the number of characters \
 in the string, the number of uppercase letters, \
 the number of lowercase letters, the number of punctuation marks,\
 the number of spaces, and the number of digits in the string."""
    if string is None:
        raise ValueError("AssertionError: Value Error")
    try:
        print(f"The text contains {len(string)} characters:")
        upper_count = sum(c.isupper() for c in string)
        print(f"{upper_count} upper letters")
        lower_count = sum(c.islower() for c in string)
        print(f"{lower_count} lower letters")
        punctuation_count = sum(is_punctuation(c) for c in string)
        print(f"{punctuation_count} punctuation marks")
        print(f"{string.count(' ')} spaces")
        digit_count = sum(c.isdigit() for c in string)
        print(f"{digit_count} digits")
    except ValueError:
        print("AssertionError: Value Error")


def main():
    """$>python building.py str | cat -e"""
    try:
        string = None
        if len(sys.argv) > 2:
            raise Exception("AssertionError: too many arguments")
        elif len(sys.argv) < 2 or sys.argv[1] == "":
            print("What is the text to count?")
            try:
                string = input() + " "
                if not string:
                    return
            except EOFError:
                return
        else:
            string = sys.argv[1]
            if not string:
                return
        analyze_string(string)
    except Exception as e:
        print(f"{e}$", file=sys.stderr)


if __name__ == "__main__":
    main()
