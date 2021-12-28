from matplotlib import pyplot as plt
import scipy.stats as ss
import numpy as np
import pandas as pd
import csv


with open("Zoopark.txt", 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split('    ') for line in stripped if line)
    with open("Zoopark.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('sample_0', 'sample_1', 'sample_2', 'sample_3', 'sample_4'))
        writer.writerows(lines)


df = pd.read_csv("Zoopark.csv")
plt.plot(x, stats.exponweib.pdf(x,exp1,k1,loc1,lam1), 'ro', lw=2)

plt.hist(df.sample_1, density=True, bins=100)
plt.hist(df.sample_2, density=True, bins=100)
plt.hist(df.sample_3, density=True, bins=100)
plt.hist(df.sample_4, density=True, bins=100)
plt.show()