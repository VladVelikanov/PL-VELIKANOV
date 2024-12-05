file = open('Начальный файл.txt')

matrix = []

for a in file.readlines():
    a = a.split()
    for b in range(len(a)):
        a[b] = int(a[b])
    matrix.append(a)

n = len(matrix)
count = 0
total = 0
for a in range(n):
    for b in range(a + 1, n):
        element = matrix[a][b]
        if element > 0:
            count += 1
        total += element

file1 = open("Итог.txt", "w")
file1.write(f'Sum: {total}\n')
file1.write(f'Count: {count}\n')