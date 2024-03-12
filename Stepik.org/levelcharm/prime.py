import sympy
def gen_simple():
    i = 1
    while True:
        yield sympy.prime(i)
        i += 1
g = gen_simple()
print(*(next(g) for _ in range(20)))