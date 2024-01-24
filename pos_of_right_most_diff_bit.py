import sys


def posOfRightMostDiffBit(m,n):
    count=1
    while True:
        print(f"bin of m : {bin(m)}")
        print(f"bin of n : {bin(n)}")
        k = m & (~(m-1))
        l = n & (~(n-1))
        print(f"bin of k : {bin(k)}")
        print(f"bin of l : {bin(l)}")
        if k & l != 0:
            count+=1
            m>>=1
            n>>=1
        else:
            print("returning count")
            print(f"bin of k : {bin(k)}")
            print(f"bin of l : {bin(l)}")
            return count 
    

m = int(sys.argv[1])
n = int(sys.argv[2])
print(posOfRightMostDiffBit(m, n))