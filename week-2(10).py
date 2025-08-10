def countZeros(matrix):
    N = len(matrix)
    count = 0
    row = 0
    col = N - 1  # Start from the top-right corner

    while row < N and col >= 0:
        if matrix[row][col] == 0:
            # If we find a zero, all elements in this column above this row are also zeros
            count += (col + 1)  # Add the number of zeros in this row
            row += 1  # Move down to the next row
        else:
            col -= 1  # Move left to the next column

    return count

# Example usage:
if __name__ == "__main__":
    matrix1 = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
    ]
    
    matrix2 = [
        [1, 1],
        [1, 1]
    ]

    print(countZeros(matrix1))  # Output: 6
    print(countZeros(matrix2))  # Output: 0
