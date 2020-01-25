"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

a = 1
b = 2
c = 3

def zwieksz_c():
    global c
    c += 1
    return c

def zwieksz_b():
    global b
    b += 1
    return b

def zwieksz_a():
    global a
    a += 1
    return a

while a ** 2 + b ** 2 != c ** 2 or a + b + c != 1000:
    if c != 997:
        zwieksz_c()
        # print(f'c: {c}')
    elif b != 499:
        c = 3
        zwieksz_b()
        # print(f'b: {b}')
    elif a != 334:
        c = 3
        b = 2
        zwieksz_a()
        print(f'a: {a}')


print(a, b, c)
print(a * b * c)




