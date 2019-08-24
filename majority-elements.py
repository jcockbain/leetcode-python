def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = collections.Counter(nums)
    for number in count:
        if count[number] > len(nums) / 2:
            return number
