#!/usr/bin/env python3
import getpass
import sys
import time

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


def to_display_format(extracted_string, positions):
    """Formats each element in the extracted string to ensure it is 2 characters wide and prints positions below them."""
    # Format extracted elements
    formatted_elements = [f"{char:>2}" for char in extracted_string]
    formatted_string = ''.join(formatted_elements)

    # Format positions, ensuring alignment with the elements above
    formatted_positions = [f"{pos+1:>2}" for pos in positions]  # pos+1 because positions are 0-based internally
    formatted_positions_string = ''.join(formatted_positions)

    return formatted_string, formatted_positions_string


def clear_last_lines_after_delay(delay=30, lines_to_clear=3):
    """Clears the specified number of lines from the console after a countdown, showing the time left."""
    for remaining in range(delay, -1, -1):
        sys.stdout.write("\033[K")  # Clear the current line
        print(f"Clearing in {remaining} seconds...")  # Display countdown
        time.sleep(1)
        if remaining > 0:
            # Move cursor up one line to overwrite the countdown next loop iteration
            sys.stdout.write("\033[1A")

    # Once countdown is complete, clear the lines including the countdown line
    for _ in range(lines_to_clear + 2):  # Include the countdown line itself in the clear
        sys.stdout.write("\033[1A")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the current line

    # Correct cursor placement: After clearing, move cursor up to the position above the first cleared line
    # This adjustment assumes the loop above leaves the cursor below the last line it cleared
    sys.stdout.flush()


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: pmask <indices>")
            sys.exit(1)

        positions_str = sys.argv[1]
        positions = extract_char_positions(positions_str)

        input_string = fetch_user_input("Enter a string of characters (it will be treated as a password): ")
        extracted_elements = extract_selected_elements(input_string, positions)
        formatted_elements, formatted_positions = to_display_format(extracted_elements, positions)

        # Print copied elements and their positions
        print("Copied elements:\033[1m\033[91m")
        print(f"{formatted_elements}\033[0m")
        print(formatted_positions)

        # Clear the last n lines after 30 seconds
        clear_last_lines_after_delay(30, 3)
    except BrokenPipeError:
        sys.stderr.close()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
