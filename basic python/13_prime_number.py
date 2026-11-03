# Check prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("Primes up to 50:", [n for n in range(1, 51) if is_prime(n)])


# Prime factors of a number
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


print("Prime factors of 84:", prime_factors(84))

# Find the next prime after the entered number
nxt = num + 1
while not is_prime(nxt):
    nxt += 1
print("Next prime after", num, "is", nxt)
