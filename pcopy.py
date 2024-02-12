#!/usr/bin/env python3
import getpass
import sys

POSITIONS_SEPARATOR = ':'


def fetch_user_input(prompt="Password: "):
    """Securely fetching a string from the user."""
    return getpass.getpass(prompt=prompt)


def extract_selected_elements(input_string, positions):
    """Copying selected elements from a string based on a list of indices."""
    return ''.join(input_string[pos] for pos in positions if pos < len(input_string))


def extract_char_positions(positions_str):
    """Parsing a string of indices provided in the format '2:5:8:10' into a list of integers."""
    if positions_str == "":
        return []
    else:
        return [int(pos) - 1 for pos in positions_str.split(POSITIONS_SEPARATOR)]  # indeksy zaczynają się od 1


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: pcopy <indices>")
            sys.exit(1)

        positions_str = sys.argv[1]
        positions = extract_char_positions(positions_str)

        input_string = fetch_user_input("Enter a string of characters (it will be treated as a password): ")
        copied_elements = extract_selected_elements(input_string, positions)

        print(f"Copied elements: \033[1m\033[91m{copied_elements}\033[0m")
    except BrokenPipeError:
        sys.stderr.close()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
