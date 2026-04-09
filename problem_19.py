#Given an integer n, return true if it is a power of two. Otherwise, return false.
#An integer n is a power of two, if there exists an integer x such that n == 2x.
def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


# Example input
n = 16

# Function call
result = isPowerOfTwo(n)

# Output
print("Output:", result)