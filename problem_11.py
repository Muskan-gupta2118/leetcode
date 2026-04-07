def plusOne(digits):
    n = len(digits)
    
    # Traverse from last digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # carry over
    
    # If all digits were 9 (e.g., 999 → 1000)
    return [1] + digits


# Example input
digits = [1, 2, 3]

# Function call
result = plusOne(digits)

# Output
print("Output:", result)