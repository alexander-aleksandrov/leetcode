def product_of_array(nums):
    res = [1] * len(nums)
    left = 1
    for i in range(1, len(nums)):
        left *= nums[i - 1]
        res[i] *= left
    right = 1
    for i in range(len(nums) - 2, -1, -1):
        right *= nums[i + 1]
        res[i] *= right
    return res