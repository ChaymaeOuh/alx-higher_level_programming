#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, (-b))
    else:
        p = 1
        for i in range(b):
            p *= a
    return (p)
