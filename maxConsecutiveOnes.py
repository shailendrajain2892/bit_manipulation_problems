import sys


def maxConsecutiveOnes(N):
    maxCount=0
    count=0
    while N:
        if N & 1 == 1: 
            count += 1
        else:
            count = 0
        N >>= 1
        maxCount = max(count, maxCount)
    return maxCount

n = int(sys.argv[1])
print(maxConsecutiveOnes(n))