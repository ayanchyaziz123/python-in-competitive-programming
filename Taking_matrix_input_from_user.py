R = int(input("Enter the number or row : "))
C = int(input("Enetr the number of column : "))
matrix = []
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()            
