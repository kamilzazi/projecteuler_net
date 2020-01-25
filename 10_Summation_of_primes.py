"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def isprime(n):
    if n < 2:
        return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n


pierwsze = []
# returns the nth prime number


def nthprime(n):
    prime = 1
    while prime < n:
        prime += 1
        if isprime(prime):
            pierwsze.append(prime)
    return pierwsze


x = nthprime(35)
print(x)
print(sum(x))
