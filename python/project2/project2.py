
def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return a

print(sum([x for x in [fib(y) for y in range(50)] if x < 4000000 and x % 2 == 0]))
