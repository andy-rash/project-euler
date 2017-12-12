import math
import operator
from functools import reduce

def prime_factors(n):
    result = []
    while n % 2 == 0:
        result.append(n)
        n /= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            result.append(i)
            print(i)
            n /= i

    if n > 2:
        result.append(n)

    return result

n = 600851475143
factors = prime_factors(n)

print("Verify: ", factors)

prod = reduce(operator.mul, factors, 1)
print(prod, " == ", n, " ?")
if prod == n:
    print("✅")
else:
    print("❌")
