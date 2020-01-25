"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

def parzyste(n):
    n = n / 2
    return n

def nieparzyste(n):
    n = 3 * n + 1
    return n


lista = []
dlugosc = 0


for liczba in range(1, 1000000):
    x = liczba
    print(liczba)
    while liczba > 1:
        lista.append(liczba)
        if liczba % 2 == 0:
            liczba = parzyste(liczba)
        elif liczba % 2 != 0:
            liczba = nieparzyste(liczba)
    lista.append(1)
    if len(lista) > dlugosc:
        dlugosc = len(lista)
        liczba_najdluzsza = x
    print(lista)
    lista = []
    print("Kamil")

print("\n")

print(dlugosc)
print(liczba_najdluzsza)
