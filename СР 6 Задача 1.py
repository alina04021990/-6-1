N=int(input(' количество чисел'))
c=0
for i in range(N):
    a=int(input('Введите целое число'))
    if a==0:
        c+=1
print(c)
