def p(n,k=5):
    from random import randint 
    if n < 2: return False
    for y in [2,3,5,7,11,13,17,19,23,29]:
       if n%y == 0: return n == y
    s, d = 0, n-1
    while d%2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(randint(2,n-1),int(d),n)
        if x == 1 or x == n-1: continue
        for r in range(1,s):
            x = (x**2) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

s=sum([2,3,5,7,11,13,17,19,23,29])
for i in range(30,int(2e6)):
    if p(int(i)):
        s += i
print(s)
