"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

def first_bad_version(n: int) -> int:
    left, right = 1, n
    while left < right:
    # Compute midpoint this way to avoid overflow when left + right
    # might exceed the integer limit in languages with fixed-size
    # integers (for example, Java or C/C++). This is mathematically
    # equivalent to (left + right)//2 but is safer and portable.
    #
    # Example (conceptual, 32-bit signed int):
    #   left = 2_000_000_000, right = 2_000_000_001
    #   (left + right)  = 4_000_000_001 -> overflows 32-bit signed int
    #   left + (right - left)//2 = 2_000_000_000 + (1)//2 = 2_000_000_000
    # The subtraction-based formula never produces the large intermediate
    # sum, so it's safe in fixed-width-int languages.
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Alternative approach using binary search
def first_bad_version_helper(left, right, result):
    if (left == right):
        return result
    # Note: (left + right)//2 is equivalent mathematically but may
    # overflow in languages with fixed-size integers. Prefer the
    # subtraction-based midpoint calculation for portability.
    # Example (conceptual): left=2_000_000_000, right=2_000_000_100
    #   (left + right) = 4_000_000_100 -> may overflow 32-bit signed int
    #   left + (right - left)//2 = 2_000_000_000 + 100//2 = 2_000_000_050
    mid = (left + right)//2
    if isBadVersion(mid) == True:
        result = mid
        return first_bad_version_helper(left, mid, result)
    else:
        return first_bad_version_helper(mid+1, right, result)
    
def first_bad_version(n: int) -> int:
    return first_bad_version_helper(1, n, n)