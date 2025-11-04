"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
def contains_duplicate(nums: list[int]) -> bool:
    distinct_nums = set(nums)
    return len(distinct_nums) != len(nums)

# Alternative approach using a set to track seen numbers
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False