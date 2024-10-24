k=int(input('Ведите число'))
v=int(input('Ведите число'))
if v<2 and k==1:
    B=v-k+1
    print(B)
elif k>v:
    B=k**2+v**2
    print(B)
else:
    B=k**2+v
    print(B)
