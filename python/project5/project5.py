for i in range(20,int(1e9),20):
    b=0
    for x in [3,6,7,8,9,11,12,13,14,15,16,17,18,19]:
        if i%x:
            b=1;break
    if not b:
        print(i);break
