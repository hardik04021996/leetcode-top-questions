"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in t:
        count = char_count.get(char, 0)
        if count == 0:
            return False
        char_count[char] -= 1
    return True

# Alternative approach using sorting
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
