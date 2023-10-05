import numpy as np
x1=list(map(int, input().split()))
y1=list(map(int, input().split()))
x = np.array(x1)
y = np.array(y1)

A = np.vstack([x, np.ones(len(x))]).T
k, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('коэффицент k =', k,'коэффицент b =', b)
