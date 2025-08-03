# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1, ptr2 = 0,0
        while ptr1<len(s) and ptr2<len(t):
            if s[ptr1] == t[ptr2]:
                ptr1+=1
            ptr2+=1
        return ptr1==len(s)

# Example usage
sol = Solution()
result = sol.isSubsequence("abc", "ahbgdc")
print(result)  # Output: True