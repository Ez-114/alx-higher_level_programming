#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv_len = len(argv)

    if argv_len == 1:
        print("0 arguments.")

    elif argv_len == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))

    elif argv_len > 2:
        # to execlude the program name
        print("{0:d} arguments:".format(argv_len - 1))

        for i in range(1, argv_len):
            print("{0:d}: {1:s}".format(i, argv[i]))
