import getpass
import sys

POSITIONS_SEPARATOR = ':'


def fetch_user_input(prompt="Password: "):
    """Bezpieczne pobieranie ciągu znaków od użytkownika."""
    return getpass.getpass(prompt=prompt)


def extract_selected_elements(input_string, positions):
    """Kopiowanie wybranych elementów z ciągu na podstawie listy indeksów."""
    return ''.join(input_string[pos] for pos in positions if pos < len(input_string))


def extract_char_positions(positions_str):
    """Parsowanie ciągu indeksów podanych w formacie '2:5:8:10' na listę liczb całkowitych."""
    if positions_str == "":
        return []
    else:
        return [int(pos) - 1 for pos in positions_str.split(POSITIONS_SEPARATOR)]  # indeksy zaczynają się od 1


def main():
    try:
        if len(sys.argv) != 2:
            print("Użycie: pcopy <indeksy>")
            sys.exit(1)

        positions_str = sys.argv[1]
        positions = extract_char_positions(positions_str)

        input_string = fetch_user_input("Podaj ciąg znaków (będzie traktowany jako hasło): ")
        copied_elements = extract_selected_elements(input_string, positions)

        print(f"Skopiowane elementy: {copied_elements}")
    except BrokenPipeError:
        sys.stderr.close()
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

