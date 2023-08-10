#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    arg_index = len(sys.argv) - 1
    if arg_index == 1:
        print("{} argument:".format(arg_index))
    elif arg_index == 0:
        print("{} arguments.".format(arg_index))
    else:
        print("{} arguments.".format(arg_index))
    for num in range(arg_index):
        print("{}: {}".format(arg_index - 1, argv[arg_index - 1]))
