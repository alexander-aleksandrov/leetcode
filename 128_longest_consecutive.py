def longest_consecutive(nums):
    nums_sorted  = nums_sorted(set(nums))
    longest = 0
    current = 1
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)