import numpy as np
import math as mp
n=15
x=np.random.rand(15)
y=mp.random.randint(0,1,15)


def val1(a,b):
    ans=(a*(mp.log(b,2))+ (1-a)*(mp.log(1-b,2)))
    return ans

summ=0
for i in range(15):
    summ = summ + val1(x[1],y[1])


final = (-1/n)*(summ)

print(final)