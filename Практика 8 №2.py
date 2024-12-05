martix = [[15, 43, 14, 54, 73],[16, 324, 564, 3, 17],[256, 4, 7, 16, 34]]

newmatrix = []


for i in martix:
    max_index = 0
    min_index = 0
    max_number = -100
    min_number = 100
    for j in range(len(i)):
        n = i[j]
        if n < min_number:
            min_number = n
            min_index = j
        elif n > max_number:
            max_number = n
            max_index = j
    perv = i[0]
    poslednii = i[-1]
    i[0] = min_number
    i[-1] = max_number
    i[min_index] = perv
    i[max_index] = poslednii
    newmatrix.append(i)

print(newmatrix)