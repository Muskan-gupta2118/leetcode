#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly
def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        # Fill middle values
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


# Example input
numRows = 5

# Function call
result = generate(numRows)

# Output
print("Pascal's Triangle:")
for row in result:
    print(row)