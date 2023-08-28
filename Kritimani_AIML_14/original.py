from numpy import median
import pandas as pd 
df = pd.read_csv(r"/Users/kritimanileishangthem/Applied statistics/assing/original.csv")
xi = df['rating']
fi = df['frequency']

fixi = fi * xi 

mean = fixi.sum()/fi.sum()

print(f'Mean = {mean}')

# median
cf = []
scf=0
for i in fi :
    scf += i
    cf.append(scf)


n2 = fi.sum()/2  # half of obersevation


# # finding the value of rating in c_frequency
for i in cf :
    if n2 < i :
        c_f = i
        break
# print(f'The value of the c-freq {c_f}')    

for n,i in enumerate(cf) :
   if i == c_f :
       ind = n
#    print(n,i)
median = ind
print(f'Median = {median}')

mode = 3 * median - 2 * mean
print(f'Mode = {mode}')

import matplotlib.pyplot as plt

plt.plot([mean]*10)

plt.show()