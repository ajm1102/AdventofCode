import numpy as np

Numbers = np.loadtxt("1.txt")

i = 0
a = 0
b = 1
c = 0
while i < (len(Numbers) - 1):
    if Numbers[b] > Numbers[a]:
        c = c + 1
    b = b + 1
    a = a + 1
    i = i + 1
print(c)