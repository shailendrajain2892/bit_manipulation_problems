import sys


def isSparse(n):
    print(f"bin repr : {bin(n)}")
    while n:
        if n&1 and n>>1&1 :
            return False
        n>>=1
    return True

print(isSparse(int(sys.argv[1])))