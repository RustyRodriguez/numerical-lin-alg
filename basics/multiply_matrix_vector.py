
def multiply_matrix_vector(A, x):
    m, n = len(A), len(A[0])

    result = [0.0] * m

    for i in range(m):
        total = 0.0
        for j in range(n):
            total += A[i][j] * x[j]

        result[i] = total

    return result

if __name__ == "__main__":
    matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
    vector = [1, 2, 3]
    print(multiply_matrix_vector(matrix, vector))