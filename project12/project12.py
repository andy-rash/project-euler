from functools import reduce
def f(n):
    return set(reduce(list.__add__, ([i,n//i] for i in range(1,int(n**0.5)+1) if n % i == 0)))

for i in range(1,int(1e6)):
    if len(f(sum(range(1,i+1)))) > 500:
        print(sum(range(1,i+1)))
        break
