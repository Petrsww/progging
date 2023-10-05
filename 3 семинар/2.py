n=int(input())
import numpy as np
d=[]
def dels(n):
    while n%2==0:
        d.append(2)
        n=n//2
    for i in range(3, int(np.sqrt(n))+1, 2):
        while n%i==0:
            d.append(i)
            n=n//i
    return d
print(dels(n))
