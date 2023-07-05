def maxProduct(self, nums: list) -> int:
    res = max(nums)
    currMax, currMin = 1, 1
    for n in nums:
        if n == 0:
            currMax, currMin = 1, 1
            continue
        tmpMax = n * currMax
        currMax = max(n * currMax, n * currMin, n)
        currMin = min(tmpMax, n * currMin, n)
        res = max(res, currMax)
    return res
