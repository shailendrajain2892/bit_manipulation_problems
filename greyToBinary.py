import sys


def greyToBinary(n):
    mask=n
    while mask:
        mask>>=1
        n^=mask
    return n

print(greyToBinary(int(sys.argv[1])))