def transpose_matrix(mat):
    n = len(mat)

    # Transpose the matrix in place
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# Example usage:
mat1 = [[1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3],
         [4, 4, 4, 4]]

mat2 = [[1, 2],
         [9, -2]]

transpose_matrix(mat1)
transpose_matrix(mat2)

print(mat1)  # Output: [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(mat2)  # Output: [[1, 9], [2, -2]]
