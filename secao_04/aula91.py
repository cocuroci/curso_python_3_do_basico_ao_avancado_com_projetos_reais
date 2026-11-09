# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, max=10):
    while True:
        yield n # Pausa
        n += 1

        if n > max:
            return # Sai do while

        

gen = generator(n=10, max=25)
for n in gen:
    print(n)
