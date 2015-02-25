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

if divisor_sum == n:
    print(str(n) + " is perfect.")
else:
    print(str(n) + " is not perfect.")
