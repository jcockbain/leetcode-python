
def singleNumber(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]


print(singleNumber([2, 4, 4, 5, 5]))
