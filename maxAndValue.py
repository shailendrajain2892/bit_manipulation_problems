def checkBitsCount(mask, arr):
    count=0
    for n in arr:
        if n&mask == mask:
            count+=1
    return count

def maxAndValue(arr):

    result = 0 
    mask = 0
    for bt in range(31, -1, -1):
        # print(f'Running for bit : {i}')
        mask = 1<<bt | result
        count = checkBitsCount(mask, arr)
        if count >= 2:
            result |= mask
    return result

arr = [4, 8, 12, 16]
print(maxAndValue(arr))