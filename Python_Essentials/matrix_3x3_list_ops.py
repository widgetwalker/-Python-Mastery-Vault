def anh(alpha, beta):
    res = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

    for i in range(3):
        res[i][i] = alpha[i][i] * beta[i][i]

    return res

# Example values for the diagonal matrices
alpha = [[4, 0, 0],
           [0, 2, 0],
           [0, 0, 1]]
beta = [[1, 0, 0],
           [0, 3, 0],
           [0, 0, 4]]

# Multiply the diagonal matrices
result = anh(alpha, beta)

# Print the resulting matrix
print("alpha:")
for row in alpha:
    print(row)

print("\nbeta:")
for row in beta:
    print(row)

print("\nResult of the Multiplication:")
for row in result:
    print(row)