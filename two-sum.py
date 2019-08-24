def two_sum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        print(n)
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i


print(two_sum([1, 2, 4, 5], 9))
