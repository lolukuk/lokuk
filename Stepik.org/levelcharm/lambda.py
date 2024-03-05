def type_format(tp=''):
    def t_format(string):
        nonlocal tp
        string = list(map(int, string.split()))
        return (tuple(string), list(string))[tp == 'list']

    return t_format
n = type_format(input())
print(n(input()))