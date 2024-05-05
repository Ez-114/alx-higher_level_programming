#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    result_sum = 0

    if argc == 0:
        print("{:d}".format(result_sum))
    else:
        for i in range(argc):
            result_sum += int(sys.argv[i + 1])
        print("{:d}".format(result_sum))
