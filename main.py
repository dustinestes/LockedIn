def summed(nums):
    if len(nums) == 0:
        return 0

    total = 0
    for n in nums:
        total += n

    return total