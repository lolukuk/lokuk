from functools import wraps

def func_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return sum(res)
    return wrapper

@func_decorator
def get_list(s):
    """Функция для формирования списка целых значений"""
    return list(map(int,s.split()))

print(s)
