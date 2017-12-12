def p(x):return False if x==0 else str(x)==str(x)[::-1]
print(max([x*y for x in range(999) for y in range(999) if p(x*y)]))
