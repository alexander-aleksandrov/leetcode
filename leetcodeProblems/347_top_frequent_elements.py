def top_frequent(nums, k):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    return sorted(d, key=lambda x: d[x], reverse=True)[:k]
