'''
Created on Dec 2, 2016

@author: UnmeshVinchurkar
'''

import matplotlib.pyplot as plt
from sklearn.utils import check_random_state
from src.LinearRegression import *

n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50. * np.log(1 + np.arange(n))   

lr = LinearRegression(0.0001, x, y);
lr.train();

print(lr.getParams());
# Plot outputs
plt.scatter(x, y, color='black')

yy = [];
xx = [];
for i in x:
     yy.append(lr.estimate(i))
     xx.append(i)
    
plt.scatter(xx, yy, color='blue')

plt.show()



