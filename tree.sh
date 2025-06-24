#!/bin/bash

# Read .gitignore and create a list of patterns to exclude
exclude_patterns=$(grep -v '^#' .gitignore | grep -v '^$' | tr '\n' '|' | sed 's/|$//')

# Add terraform state files to the exclude patterns
exclude_patterns="$exclude_patterns|terraform.tfstate|terraform.tfstate.backup"

# Run the tree command with the exclude patterns
tree -I "$exclude_patterns" --noreport