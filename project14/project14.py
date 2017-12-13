def c(x):
    r = 0
    while x >= 1:
        if x == 1:
            r += 1
            break
        if x%2 == 0: 
            r += 1
            x = x // 2
        else: 
            r += 1
            x = 3 * x + 1
    return r

r = [(i,c(i)) for i in range(int(1e6),1,-1)]

from operator import itemgetter
print(max(r,key=itemgetter(1)))
