import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# Проверка симметричности относительно главной диагонали
print(["НЕТ", "ДА"][is_symmetric := all(lst_in[i][j] == lst_in[j][i] for i in range(len(lst_in)) for j in range(len(lst_in)))])
