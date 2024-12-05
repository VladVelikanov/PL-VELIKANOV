def maximum():
    x = int(input())
    if x == 0: return 0
    else: return max(x, maximum())
print(maximum())