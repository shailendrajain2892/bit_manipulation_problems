import sys


def posOfRightMostDiffBit(m,n):
    xor_result = m ^ n 

    if xor_result == 0 : 
        return -1 
    
    count=1
    while xor_result & 1 != 1:
        count+=1
        xor_result>>=1
    
    return count

m = int(sys.argv[1])
n = int(sys.argv[2])
print(posOfRightMostDiffBit(m, n))