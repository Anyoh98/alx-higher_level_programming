#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        from magic_calculation_102 import add, sub
        c = 0
        if a < b:
            c = add(a, b)
            for i in range(4, 6):
                c = add(c, i)
        else:
            c = sub(a, b)
        return(c)
