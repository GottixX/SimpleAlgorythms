p = input("Enter p: ")
p = int(p)


twins = []

twin_1 = p - 2
twin_2 = p + 2
pot_twins = [twin_1] + [twin_2]
start = 2

for twin in pot_twins:

    is_prime = True
    
    if twin == 1:
        is_prime = False
    while start < twin:
        if twin % start == 0:
            is_prime = False
            break
        start = start + 1

    if is_prime:
        twins = twins + [twin]


if len(twins) == 2:
    print("Twin primes with " + str(p) + ":")
    print(twins[0])
    print(twins[1])
elif len(twins) == 1:
    print(twin[0])
else:
    print("No prime twins found")
