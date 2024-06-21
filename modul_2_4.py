from typing import List, Any

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        if i != 1:
            primes.append(i)

print(primes)
print(not_primes)
