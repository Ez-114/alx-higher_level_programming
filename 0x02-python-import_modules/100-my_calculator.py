#!/usr/bin/python3
if __name__ == "__main__":
    # import needed modules
    import sys
    import calculator_1 as clc

    # validate argv == 3
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # store the args in their correct type
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    op = sys.argv[2]

    # Check if the operator passed is available
    if op == "+":
        result = clc.add(a, b)
    elif op == "-":
        result = clc.sub(a, b)
    elif op == "*":
        result = clc.mul(a, b)
    elif op == "/":
        result = clc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, result))
