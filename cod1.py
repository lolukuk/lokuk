def sqrt(x):

    left, right = 1, x
    while left <= right:
        num = (left + right) // 2
        if num ** 2 == x:
            return num
        elif num ** 2 < x:
            left = num + 1
        else:
            right = num - 1

    return right

print(sqrt(36))