a=int(input('Введите число'))
b=int(input('Введите число'))
if a<b:
    for i in range(a, b):
        print(i, end=";")
else:
    for i in range(a, b-1,-1):
        print(i, end=";")