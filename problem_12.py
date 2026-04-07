def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""

    # Traverse both strings from right to left
    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        # Add result bit
        result = str(total % 2) + result

        # Update carry
        carry = total // 2

    return result


# Example input
a = "1010"
b = "1011"

# Function call
output = addBinary(a, b)

# Output
print("Output:", output)