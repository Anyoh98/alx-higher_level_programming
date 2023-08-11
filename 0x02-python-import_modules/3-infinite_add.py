#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_index_count = len(sys.argv) - 1
    if arg_index_count == 0:
        print("0")
    else:
        arguments = sys.argv[1:]
        total_sum = 0
        for arg in arguments:
            total_sum += int(arg)
        print("{}".format(total_sum))
