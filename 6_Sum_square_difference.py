"""The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

suma_kwadr = 0
suma = 0

for i in range(1, 101):
    suma_kwadr += i ** 2

for i in range(1, 101):
    suma += i

print(suma_kwadr)
suma1 = suma ** 2
print(suma1)
print(suma1 - suma_kwadr)