def count(x, n):
    if n == 0: return 1
    return (x * count(x, n - 1)) / n
print(count(15, 4))