import sys


def swapBits(n):

    even_mask = 0xAAAAAAAA

    odd_mask = 0x55555555
    """ 
    - by doing even mask we are preserving the all the event bits
    - since we want to swap , so we do right shift by 1
    
    """
    even_bits = (n & even_mask)>>1

    """
    - by doing odd mask we are preserving the all odd bits
    - since we want to swap, we do left shift by 1
    """
    odd_bits = (n&odd_mask)<<1

    # combine all the odd bits and even bits with OR opertaion to get the final output 
    return even_bits | odd_bits

n = int(sys.argv[1])
print(swapBits(n))