import unittest
from pcopy import extract_selected_elements, extract_char_positions


class ExtractSelectedElementsTests(unittest.TestCase):
    def test_given_alternate_positions_when_extracting_then_return_alternate_characters(self):
        # Given
        input_string = "abcdef"
        positions = [0, 2, 4]

        # When
        result = extract_selected_elements(input_string, positions)

        # Then
        self.assertEqual(result, "ace")

    def test_given_odd_positions_when_extracting_then_return_characters_at_odd_positions(self):
        # Given
        input_string = "123456"
        positions = [1, 3, 5]

        # When
        result = extract_selected_elements(input_string, positions)

        # Then
        self.assertEqual(result, "246")

    def test_given_empty_input_string_when_extracting_then_return_empty_string(self):
        # Given
        input_string = ""
        positions = [0, 1, 2]

        # When
        result = extract_selected_elements(input_string, positions)

        # Then
        self.assertEqual(result, "")

    def test_given_empty_positions_when_extracting_then_return_empty_string(self):
        # Given
        input_string = "123456"
        positions = []

        # When
        result = extract_selected_elements(input_string, positions)

        # Then
        self.assertEqual(result, "")

    def test_given_positions_outside_range_when_extracting_then_ignore_those_positions(self):
        # Given
        input_string = "123456"
        positions = [10]  # Index outside the range

        # When
        result = extract_selected_elements(input_string, positions)

        # Then
        self.assertEqual(result, "")


class ExtractCharPositionsTests(unittest.TestCase):
    def test_given_standard_format_positions_when_extracting_then_return_correct_positions_list(self):
        # Given
        positions_str = "1:2:3"

        # When
        result = extract_char_positions(positions_str)

        # Then
        self.assertEqual(result, [0, 1, 2])

    def test_given_single_position_when_extracting_then_handle_as_single_position(self):
        # Given
        positions_str = "10"

        # When
        result = extract_char_positions(positions_str)

        # Then
        self.assertEqual(result, [9])

    def test_given_empty_positions_string_when_extracting_then_return_empty_list(self):
        # Given
        positions_str = ""

        # When
        result = extract_char_positions(positions_str)

        # Then
        self.assertEqual(result, [])

    def test_given_invalid_input_when_extracting_then_raise_value_error(self):
        # Given
        positions_str = "a:b:c"

        # When / Then
        with self.assertRaises(ValueError):
            extract_char_positions(positions_str)

