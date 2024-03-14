#!/usr/bin/python3

# Prevent execution when imported
if __name__ == "__main__":
    import sys  # To use argv

    total = 0
    for arg in sys.argv:
        if arg[:2] == "./":
            continue
        total += int(arg)
    print(total)
