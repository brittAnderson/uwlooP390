# Terminal Scripting Exercise

## Objective
Create a simple bash script that demonstrates basic shell scripting skills including user input, command execution, and output formatting.

## Requirements
Create a file called `student_script.sh` that does the following:

1. Prompts the user for their name
2. Greets the user by name
3. Counts the total number of files and directories in the user's home directory
4. Displays this count in a friendly message

## Example Output
```
What is your name? Alice
Hello, Alice!
You have 127 items (files and directories) in your home directory.
```

## Hints
- Use `read` to get user input
- Use `ls -A ~` to list all items in home directory (including hidden files)
- Use `wc -l` to count lines
- Remember to make your script executable with `chmod +x student_script.sh`
- Include a shebang line (`#!/bin/bash`) at the top

