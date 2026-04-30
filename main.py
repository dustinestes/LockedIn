def find_minimum(nums):
    minimum = float("inf")
    if not nums:
        return None
    
    for n in nums:
        minimum = n if n < minimum else minimum

    return minimum