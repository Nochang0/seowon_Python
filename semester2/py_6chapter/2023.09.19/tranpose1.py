# 294P

tranposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래 행렬=", matrix)

# 열의 개수만큼 반복한다.
for i in range(len(matrix[0])):
    tranposed_row = []
    for row in matrix:
        tranposed_row.append(row[i])
    tranposed.append(tranposed_row)
    
print("전치 행렬=", tranposed)