def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid   # store possible answer
            left = mid + 1
        else:
            right = mid - 1

    return ans


# Example input
x = 8

# Function call
result = mySqrt(x)

# Output
print("Output:", result)