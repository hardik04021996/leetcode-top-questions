# https://leetcode.com/problems/summary-ranges

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start, end = 0,0
        if len(nums)==0:
            return nums
        if len(nums)==1:
            return [f'{nums[0]}']
        i = 1
        while i < len(nums):
            if nums[end] + 1 == nums[i]:
                end = i
                i+=1
            else:
                ranges.append(f'{nums[start]}->{nums[end]}' if start!=end else f'{nums[start]}')
                end = i
                start = end
                i += 1
        ranges.append(f'{nums[start]}->{nums[end]}' if start!=end else f'{nums[start]}')
        return ranges

# Example usage
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))  # Output: ["0->2", "4->5", "7"]
print(sol.summaryRanges([0,2,3,4,6,8,9]))  # Output: ["0", "2->4", "6", "8->9"]
print(sol.summaryRanges([]))  # Output: []
print(sol.summaryRanges([1]))  # Output: ["1"]