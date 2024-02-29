def decor(f):
    def wrapper():
        print('Код декоратора')
        f()
        print('Второй код')
    return wrapper

@decor
def make():
    enter = input('Пиши')
    print(enter)

print('ees')
make()