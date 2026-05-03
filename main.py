def find_max(nums):
    if not nums:
        return None
    
    highest_num = float("-inf")
    for n in nums:
        if n > highest_num:
            highest_num = n

    return highest_num
