
import numpy as np
def get_anti_diagonals(matrix):
    n = len(matrix)
    anti_diagonals = []

    for k in range(n):
        diagonal = []
        i, j = k, 0

        while i >= 0 and j < n:
            diagonal.append(matrix[i][j])
            i -= 1
            j += 1

        anti_diagonals.append(diagonal)

    for k in range(1, n):
        diagonal = []
        i, j = n - 1, k

        while i >= 0 and j < n:
            diagonal.append(matrix[i][j])
            i -= 1
            j += 1

        anti_diagonals.append(diagonal)
    max_length = max(len(diagonal) for diagonal in anti_diagonals)
    for diagonal in anti_diagonals:
        diagonal.extend([0] * (max_length - len(diagonal)))

    return anti_diagonals
row=int(input("enter row count: "))
column=int(input("enter column count: "))
array=list(map(int,input("enter matrix values: ").split()))
matrix=np.array(array).reshape(row,column)

anti_diagonals = get_anti_diagonals(matrix)
for diagonal in anti_diagonals:
    print(' '.join(str(num) for num in diagonal))
