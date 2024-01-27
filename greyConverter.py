import sys


def greyConverter(n):
    ##Your code here
    n^=n>>1
    return n

print(greyConverter(int(sys.argv[1])))