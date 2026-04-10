#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
def getRow(rowIndex):
    row = [1]  # first row

    for i in range(1, rowIndex + 1):
        new_row = [1] * (i + 1)

        for j in range(1, i):
            new_row[j] = row[j-1] + row[j]

        row = new_row

    return row


# Example input
rowIndex = 4

# Function call
result = getRow(rowIndex)

# Output
print("Output:", result)
