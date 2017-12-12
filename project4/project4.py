print(max([x*y for x in range(999) for y in range(999) if x*y!=0 and str(x*y)==str(x*y)[::-1]]))
