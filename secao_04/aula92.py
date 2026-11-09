# Yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    print('Acabou gen1()')
    yield 4
    yield 5
    yield 6

gen = gen2()
for value in gen:
    print(value)