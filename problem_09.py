#Given two strings needle and haystack,
#  return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)

    
    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i
    
    return -1
haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))  # Output: 2