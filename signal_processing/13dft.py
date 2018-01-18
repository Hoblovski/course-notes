"""DFT in 13 lines of code.

sample input:```
5
cos(2*pi*n/5)```

sample output:```
[[-0. +0.j]
 [ 2.5-0.j]
 [ 0. -0.j]
 [ 0. +0.j]
 [ 2.5+0.j]]
```

"""
        
import numpy as np
from math import *

N        = int(input())
L        = N
funcrepr = input().strip()
f        = eval("lambda n :" + funcrepr)
x        = np.array([f(n) for n in range(N)])
W_N      = e**((-2*pi/N) * 1j)
W        = [[W_N**(n*k) for k in range(N)] for n in range(L)]
y        = np.matmul(W, x)
np.set_printoptions(precision=2, suppress=True)
print(np.reshape(y, [-1, 1])) # transposed looks better
