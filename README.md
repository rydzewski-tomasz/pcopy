![GitHub Actions Status](https://github.com/rydzewski-tomasz/pcopy/actions/workflows/pcopy-test.yml/badge.svg)

# Pcopy - An Application for Copying Selected Elements of a String

Pcopy is a simple console application written in Python that allows the user to safely copy selected elements from a given string. By using a password as input, users can confidently process sensitive data such as API keys or passwords without the risk of displaying them on the screen.

## Requirements

- Python 3.10 or newer

## Installation

To get started with `pcopy`, clone this repository and make sure you have Python installed.

Upon running the script, you will be prompted to enter a string. The copied elements will not be displayed on the screen; instead, they will be stored in the system clipboard (if you decided to implement this feature).

## Usage Example

To use the application, run the `pcopy.py` script from the command line, providing the indexes of elements to copy, separated by colons:

## License

This project is made available under the MIT License, which means you are free to use, modify, and distribute it.