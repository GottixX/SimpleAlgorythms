n = input("Enter n: ")
n = int(n)

divisor_sum = 0
numbers = range(1, n - 1)
divisors = []

for number in numbers:
    if n % number == 0:
        divisors = divisors + [number]

for div in divisors:
    divisor_sum += div



print(divisor_sum)
