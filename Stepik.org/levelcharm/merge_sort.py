def merge(lst1, lst2):
    res, i, j = [], 0, 0
    while lst1 and lst2:
        res.append((lst1, lst2)[lst1[-1] < lst2[-1]].pop())
    return lst1 + lst2 + res[::-1]

def merge_sort(lst):
    hl = len(lst) // 2
    return hl and merge(merge_sort(lst[:hl]), merge_sort(lst[hl:])) or lst

lst = list(map(int, input().split()))
print(*merge_sort(lst))

# 7.7 Подвиг 8 - Решить