# write a program to find the longest common prefix string amongst an array of string
# if there is a common prefix, return an empty string. 
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
            
    return prefix
strings = ["flower", "flow", "flight"]
result = longestCommonPrefix(strings)
print("Longest Common Prefix:", result)
