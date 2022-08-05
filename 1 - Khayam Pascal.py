n = int(input("N: "))
triangle = [[0]*n for i in range(n)]

for i in range(n):
    triangle[i][0] = 1
    for j in range(1, i+1):
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

for i in range(n):
    for j in range(n):
        if triangle[i][j] != 0: print(triangle[i][j], end='\t')
    print()


