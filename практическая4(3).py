a = int(input('введите число '))
b = int(input('введите число '))
if a>b:
    for i in range (b, a+1):
        if i%2!=0:
            print(i)