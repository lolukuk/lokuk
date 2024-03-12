import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = []
# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!
for i in lst_in:
    lst2D.append(i).split(",")