n = input("Enter n: ")
n = int(n)

numbers = range(1, n - 1)
divisors = []
for number in numbers:
    if n % number == 0:
        divisors = divisors + [number]

print(divisors)
