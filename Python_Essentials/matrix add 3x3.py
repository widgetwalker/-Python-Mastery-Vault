# Define matrices
matrix1 = [[1, 2, 3], 
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4], 
           [3, 2, 1]]

# Initialize result matrix
result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Perform element-wise matrix addition  
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print result 
for r in result:
    print(r)