import math
import sys


def countBitsFlip(a,b):
    xor_result = a ^ b
    
    count=0
    while xor_result:
        count+=xor_result & 1
        xor_result >>= 1
        
    return count

a = int(sys.argv[1])
b = int(sys.argv[2])
print(countBitsFlip(a, b))