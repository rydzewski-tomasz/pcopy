#!/bin/bash

# Define the path to the Python script and the command name
PYTHON_SCRIPT_PATH="../pmask.py"
COMMAND_NAME="pmask"
TARGET_DIR=~/bin

# Create the target directory if it does not exist
mkdir -p "$TARGET_DIR"

# Check if the Python script exists at the given path
if [ ! -f "$PYTHON_SCRIPT_PATH" ]; then
    echo "$PYTHON_SCRIPT_PATH not found."
    exit 1
fi

# Add a shebang line to the Python script if it doesn't already have one
grep -q '^#!/usr/bin/env python3' "$PYTHON_SCRIPT_PATH" || sed -i '1i#!/usr/bin/env python3' "$PYTHON_SCRIPT_PATH"

# Copy the Python script to the target directory and rename it, then make it executable
cp "$PYTHON_SCRIPT_PATH" "$TARGET_DIR/$COMMAND_NAME"
chmod +x "$TARGET_DIR/$COMMAND_NAME"

