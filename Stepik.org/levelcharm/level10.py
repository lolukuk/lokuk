#tuple = tuple(range(20, 51))
#print(tuple[::-2])

def func():
    b = input('Cколько?')
    y = input('Число')
    x = input('Строка')
    z = y + x
    for i in b:
        print(func(y, x))


func(1,2)