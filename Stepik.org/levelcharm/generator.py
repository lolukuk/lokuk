def get_data_fig(*args, **kwargs):
    per = 0
    order = ['type', 'color', 'closed', 'width']
    n = [kwargs[i] for i in order if i in kwargs]
    for i in args:
        per += i
    return (per,) + tuple(n)

print(get_data_fig(1,23,4,5,5,7, width=2, type=True, color=1, closed=False))