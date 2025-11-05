"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""
def move_zeroes(nums: list[int]) -> None:
    k = 0  # Pointer for the position of the next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    # Fill the remaining positions with zeros
    for i in range(k, len(nums)):
        nums[i] = 0

# Alternative approach using two pointers
def move_zeroes(nums: list[int]) -> None:
    nzi = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            if nzi != i:
                nums[nzi], nums[i] = nums[i], 0
            nzi += 1