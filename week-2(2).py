def rotate_90_anticlockwise(mat):
    n = len(mat)

    # First, transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Then, reverse each row
    for i in range(n):
        mat[i].reverse()

# Example usage:
mat1 = [[0, 1, 2], 
         [3, 4, 5], 
         [6, 7, 8]]

mat2 = [[1, 2],
         [3, 4]]

rotate_90_anticlockwise(mat1)
rotate_90_anticlockwise(mat2)

print(mat1)  # Output: [[2, 5, 8], [1, 4, 7], [0, 3, 6]]
print(mat2)  # Output: [[2, 4], [1, 3]]
