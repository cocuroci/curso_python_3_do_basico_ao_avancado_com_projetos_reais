from itertools import count

c1 = count()
r1 = range(10)

print(next(c1))
print(next(c1))

print('c1 é interator', hasattr(c1, '__iter__'))
print('c1 é interavel', hasattr(c1, '__next__'))