
n=20
f=lambda x: 1 if x == 0 else f(x-1)*x

print(f(2*n)/(f(n)*f(2*n-n)))
