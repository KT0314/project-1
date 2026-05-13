import numpy as np

a = np.array(["A", "B", "C"])

b = np.array([10, 20, 30])

c = np.argmax(b)

d = np.argmin(b)

print("最大的品項:",a[c])

print("最小的品項:",a[d])

