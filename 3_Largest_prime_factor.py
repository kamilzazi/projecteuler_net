"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


liczba = 600851475143
lista = []
for i in range(2, liczba + 1):
    if liczba % i == 0:
        liczba = liczba / i
        lista.append(i)
        print(i)
    else:

        i += 1

print(lista)
