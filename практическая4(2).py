a=int(input('введите число '))
b=int(input('введите число '))

if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in reversed(range(b,a+1)):
        print(i)