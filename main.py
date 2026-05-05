def bubble_sort(nums):
    swapping = True

    while swapping:
        swapping = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapping = True

    return nums
            
