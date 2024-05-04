#!/usr/bin/python3
for i in range(26):
    # Calculate the ASCII code for the lowercase and uppercase letters
    lowercase_char = chr(ord('z') - i)
    uppercase_char = chr(ord('Z') - i)

    # Use ternary operator to choose between lowercase
    # and uppercase based on the index `i`
    char = lowercase_char if i % 2 == 0 else uppercase_char

    # Print the chosen character without a newline at the end
    print(char, end='')
