#!/usr/bin/env python3
import getpass
import sys
import time
import signal

POSITIONS_SEPARATOR = ':'
SPACES_BETWEEN_ELEMENTS = 5
CONSOLE_CLEAR_DELAY_IN_S = 30
CONSOLE_LINES_TO_CLEAR = 7
CONSOLE_LINES_TO_CLEAR_FORCE_EXIT = CONSOLE_LINES_TO_CLEAR + 2

ANSI_CODES = {
    "BOLD": "\033[1m",
    "RED": "\033[91m",
    "RESET": "\033[0m",
    "CLEAR_LINE": "\033[K",
    "CURSOR_UP": "\033[1A",
}


def main():
    # Register the signal handler for SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    try:
        if len(sys.argv) != 2:
            print("Usage: pmask <indices>")
            sys.exit(1)

        positions_str = sys.argv[1]
        positions = extract_char_positions(positions_str)

        input_string = fetch_user_input("Enter a string of characters (it will be treated as a password): ")
        extracted_elements = extract_selected_elements(input_string, positions)
        formatted_elements, formatted_positions = to_display_format(extracted_elements, positions)

        display_masked_password(formatted_elements, formatted_positions)
    except BrokenPipeError:
        sys.stderr.close()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_user_input(prompt="Password: "):
    """Securely fetching a string from the user."""
    return getpass.getpass(prompt=prompt)


def extract_selected_elements(input_string, positions):
    """Copying selected elements from a string based on a list of indices."""
    return ''.join(input_string[pos] for pos in positions if pos < len(input_string))


def extract_char_positions(positions_str):
    """Parsing a string of indices provided in the format '2:5:8:10' into a list of integers."""
    if positions_str == '':
        return []
    else:
        return [int(pos) - 1 for pos in positions_str.split(POSITIONS_SEPARATOR)]  # indexes starts with 1


def to_display_format(extracted_string, positions):
    """Formats each element in the extracted string to ensure it is 2 characters wide and prints positions below them."""
    # Format extracted elements
    formatted_elements = [f"{char:>{SPACES_BETWEEN_ELEMENTS}}" for char in extracted_string]
    formatted_string = ''.join(formatted_elements)

    # Format positions, ensuring alignment with the elements above
    formatted_positions = [f"{pos+1:>{SPACES_BETWEEN_ELEMENTS}}" for pos in positions]  # pos+1 because positions are 0-based internally
    formatted_positions_string = ''.join(formatted_positions)

    return formatted_string, formatted_positions_string


def clear_last_lines_after_delay(delay=30):
    """Clears the specified number of lines from the console after a countdown, showing the time left."""
    for remaining in range(delay, -1, -1):
        sys.stdout.write(ANSI_CODES["CLEAR_LINE"])  # Clear the current line
        print(f"Clearing in {remaining} seconds...")  # Display countdown
        time.sleep(1)
        if remaining > 0:
            # Move cursor up one line to overwrite the countdown next loop iteration
            sys.stdout.write(ANSI_CODES["CURSOR_UP"])

    clear_console_lines(CONSOLE_LINES_TO_CLEAR)  # Include the countdown line itself in the clear

    sys.stdout.flush()


def clear_console_lines(lines_to_clear):
    """Clears the specified number of lines from the console."""
    for _ in range(lines_to_clear):
        sys.stdout.write(ANSI_CODES["CURSOR_UP"])  # Move cursor up one line
        sys.stdout.write(ANSI_CODES["CLEAR_LINE"])  # Clear the current line


def signal_handler(sig, frame):
    """Handles interrupt signals such as SIGINT (Ctrl+C)."""
    print("\nForce exit detected, clearing console...")
    clear_console_lines(CONSOLE_LINES_TO_CLEAR_FORCE_EXIT)  # Adjust the number of lines to clear as needed
    sys.exit(0)  # Exit the script


def display_masked_password(formatted_elements, formatted_positions):
    print("Copied elements:" + ANSI_CODES["BOLD"] + ANSI_CODES["RED"])
    print(f"{formatted_elements}" + ANSI_CODES["RESET"])
    print(formatted_positions)
    clear_last_lines_after_delay(CONSOLE_CLEAR_DELAY_IN_S)


if __name__ == "__main__":
    main()
