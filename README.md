![GitHub Actions Status](https://github.com/rydzewski-tomasz/pmask/actions/workflows/tests.yml/badge.svg)

# pmask: Secure Password Masking Tool

## Description
pmask is a Python-based utility designed to securely fetch a string from the user (treated as sensitive information, such as a password) and copy selected elements from it based on a list of indices provided by the user. The program formats and displays the copied elements along with their positions, and automatically clears this information from the console after a short delay for enhanced security.

## Requirements
- Python 3.10 or newer
- Linux or Unix-like environment

## Installation
To install pmask, follow these steps:
1. Ensure you have Python 3 installed on your system.
2. Run the installation script with `./tools/install.sh`. This script will:
3. Command should be added to `~/bin`
4. Make sure that `~/bin` is added to $PATH

## Usage Example
To use pmask, run the following command in your terminal:
```bash
pmask "2:5:8"
```
Replace "2:5:8" with the positions of the elements you wish to copy, separated by colons. You will be prompted to enter a string (your sensitive information), and the program will display and then clear the elements after a delay.

Example:
```bash
$ pmask "2:5:8"
Enter a string of characters (it will be treated as a password):
Copied elements: 
t s t
2 5 8
```

**Note**: message will be auto clear after 30s.

## License
pmask is released under the MIT License.
