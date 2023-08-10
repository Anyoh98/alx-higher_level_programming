#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    result1 = a + b 
    result2 = a - b
    result3 = a * b
    result4 = a / b
    print("{} + {} = {}".format(a, b, result1))
    print("{} - {} = {}".format(a, b, result2))
    print("{} * {} = {}".format(a, b, result3))
    print("{} / {} = {}".format(a, b, result4))
