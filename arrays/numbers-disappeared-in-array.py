def find_not_in_array(nums):
    marked = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in marked]

# Extra solutions using algorithm trickery
