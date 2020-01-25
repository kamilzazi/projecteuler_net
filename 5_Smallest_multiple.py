"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

lista = []
number = 20

while len(lista) < 20:
    for i in range(1, 21):
        if len(lista) == 20:
            break
        if number % i != 0:
            lista = []
            number += 1
        elif number % i == 0:
            lista.append(i)
            print(number)
            print(lista)

