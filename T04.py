def is_peak(A, i, j):
    m, n = len(A), len(A[0])
    neighbors = [
        (i - 1, j),  # Up
        (i + 1, j),  # Down
        (i, j - 1),  # Left
        (i, j + 1)   # Right
    ]
    return all(A[x][y] <= A[i][j] for x, y in neighbors if 0 <= x < m and 0 <= y < n)

def find_maximal_in_col(A, col):
    max_i = max(range(len(A)), key=lambda i: A[i][col])
    return max_i

# Include left, exclude right
def find_peak_sp(A, left, right):
    
    # If the submatrix has no columns, return None.
    if left >= right:
        return None
    
    raise NotImplementedError

def print_matrix_with_peaks(A):
    m, n = len(A), len(A[0])
    
    for i in range(m):
        row_output = []
        for j in range(n):
            if is_peak(A, i, j):
                row_output.append(f"{A[i][j]}*")  # Mark peak
            else:
                row_output.append(f"{A[i][j]} ")  # Normal number
        print(" ".join(row_output))  # Print row as a formatted string

# -----------------------
# Main function
# -----------------------
if __name__ == '__main__':
    test_matrices = [
        # 1x1 matrix
        [[5]],
        
        # Single column matrix
        [
            [1],
            [3],
            [2]
        ],
        
        # One row, multiple columns
        [[1, 3, 2, 4, 1]],
        
        # 4x4 matrix
        [
            [10,  8, 10, 10],
            [14, 13, 12, 11],
            [15,  9, 11, 21],
            [16, 17, 19, 20]
        ],
        
        # 3x3 matrix with a clear peak
        [
            [10, 20, 15],
            [21, 30, 14],
            [7,  16, 32]
        ],

        # New test case: 3x5 matrix (example test case)
        [
            [6,  8, 7,  7,  1],
            [9,  3, 1,  7,  3],
            [8,  4, 5,  3,  2]
        ]
    ]
    
    for idx, A in enumerate(test_matrices):
        print(f"Test {idx + 1}: Matrix")
        print_matrix_with_peaks(A)
        
        peak = find_peak_sp(A, 0, len(A[0]))
        if peak is None:
            print("    No peak found!\n")
        else:
            i, j = peak
            print(f"    Peak found at ({i}, {j}) with value {A[i][j]}")
            if not is_peak(A, i, j):
                print("    Verification: ERROR, not a peak!\n")
