

# problem asks for smallest number evenly divisible by all numbers in [1..20]

# for loop iterates over all numbers [20..1e9] with a step of 20
# coincidentally, these are all the numbers that are evenly divisible by 20

# numbers in sub-for-loop set are those numbers that do not evenly
# divide 20
# i.e. these numbers are all numbers in [1..20] that are not divisors of 20
# i.e. all numbers [1..20] except for [1,2,4,5,10,20]

# `if i%x` will break out of the whole loop if the given i value cannot be
# evenly divided by one of the values in x

for i in range(20,int(1e9),20):
    b=0
    for x in [3,6,7,8,9,11,12,13,14,15,16,17,18,19]:
        if i%x:
            b=1;break
    if not b:
        print(i);break
