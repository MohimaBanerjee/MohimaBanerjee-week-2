def spiral_traverse(mat):
    if not mat or not mat[0]:
        return []

    result = []
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1

    return result

# Example usage:
mat1 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]

mat2 = [[2, 7, 10],
         [5, 1, 3],
         [4, 2, 8]]

mat3 = [[32, 44, 27, 23],
         [54, 28, 50, 62]]

print(spiral_traverse(mat1))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
print(spiral_traverse(mat2))  # Output: [2, 7, 10, 3, 8, 2, 4, 5, 1]
print(spiral_traverse(mat3))  # Output: [32, 44, 27, 23, 62, 50, 28, 54]
