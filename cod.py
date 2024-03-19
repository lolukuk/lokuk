
def spiral_matrix(m,n):
    result = [[0] * n for i in range(m)]
    top, bot, left, right = 0, m-1, 0, n-1
    num = 1

    while top <= bot and left <= right:
        for i in range(left, right+1):
            result[top][i] = num
            num += 1
        top += 1

        for i in range(top, bot + 1):
            result[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            result[bot][i] = num
            num += 1
        bot -= 1

        for i in range(bot, top - 1, -1):
            result[i][left] = num
            num += 1
        left += 1

    return result

m,n = 4, 5
matrix = spiral_matrix(m,n)
for i in matrix:
    print(' '.join(map(str,i)))