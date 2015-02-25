n = input("Enter n: ")
n = int(n)

digits = []
primes = [2, 3, 5, 7]
while n != 0:
    digit = n % 10

    digits = digits + [digit]

    n = n // 10

has_prime_digit = False

for digit in digits:
    if digit in primes:
        has_prime_digit = True
        break

if has_prime_digit:
    print("Yse, I found prime digits")
else:
    print("Sorry! No prime digits")
