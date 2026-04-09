def isPalindrome(s):
    cleaned = ""

    # Keep only alphanumeric characters and convert to lowercase
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    # Check palindrome
    return cleaned == cleaned[::-1]


# Example input
s = "A man, a plan, a canal: Panama"

# Function call
result = isPalindrome(s)

# Output
print("Output:", result)