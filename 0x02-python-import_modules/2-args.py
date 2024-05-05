#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{:d} {}:".format(argc, "arguments" if argc > 1 else "argument"))

        for i in range(argc):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
