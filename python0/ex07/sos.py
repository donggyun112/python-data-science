import sys


def convert_to_morse(n):
    """ convert_to_morse(n: str) -> str \
        This function takes a character as an argument \
        and returns the morse code for that character."""
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    return MORSE_CODE_DICT[n]


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError()
        string = str(sys.argv[1])
        morse_string = map(convert_to_morse, string.upper())
        print(" ".join(morse_string))
    except AssertionError as e:
        print(f"{e}", file=sys.stderr)
    except ValueError:
        print("AssertionError: the arguments are bad", file=sys.stderr)
    except Exception as e:
        print(f"{e}", file=sys.stderr)


if __name__ == "__main__":
    main()
