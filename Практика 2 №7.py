import math
x=(input("Введите переменную x:"))
y=(input("Введите переменную y:"))
z=(input("Введите переменную z:"))
s=5*math.atan2(x)-math.acos(x)/4*(x+3*math.fabs(x-y)+x**2)/(math.fabs(x-y)*z+x**2)
print(s)