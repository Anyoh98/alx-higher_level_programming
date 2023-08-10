#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_index = len(sys.argv) - 1
    if arg_index == 1:
        print("1 argument:")
    elif arg_index == 0:
        print("0 arguments.")
    else:
        print("{} arguments.".format(arg_index))
    for num in range(arg_index):
        print("{}: {}".format(num + 1, sys.argv[num + 1]))
