matrix =  [[1, 2, 3, 1],[4, 5, 6, 0],[7, 8, 9, -1]]
transpose = lambda matrix: [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose(matrix))
