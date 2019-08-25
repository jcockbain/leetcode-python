def moveZeroes(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    print(nums)

(moveZeroes([1, 2, 0, 4, 5, 0, 3, 2, 1]))
