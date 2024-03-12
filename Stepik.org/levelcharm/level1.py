d = dict((c.split('=') for c in open(0)))
print(*sorted(d, key=lambda x: int(d[x]), reverse=True))