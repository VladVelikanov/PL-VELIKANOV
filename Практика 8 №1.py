matrix = [[15, 35, 64],[32, 77, 15],[25, 79, 21]]
n = len(matrix)
count = 0
total = 0
for a in range(n):
    for b in range(a + 1, n):
        element = matrix[a][b]
        if element > 0:
            count += 1
        total += element

print("Итоговая сумма:", total)
print("элементов >0:", count)