def divideArray(nums, k):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(0, n, 3):
        group = nums[i:i+3]
        if group[-1] - group[0] > k:
            return []
        res.append(group)
    return res