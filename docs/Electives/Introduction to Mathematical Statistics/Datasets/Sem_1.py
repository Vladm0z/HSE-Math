import matplotlib.pyplot as plt
import numpy as np
import random

np.random.seed()
#f = lambda a: a ** 2
f = lambda a: a ** -0.5
x = f(np.random.uniform(0.0, 1.0, 1000))

plt.hist(x, density=True, bins=25)
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()

#N, s = 1000, 0
#for i in range(N):
#	s += 1/(random.random())**0.5
#print(s/N)