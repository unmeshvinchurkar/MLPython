'''
Created on Dec 3, 2016

@author: UnmeshVinchurkar
'''
import matplotlib.pyplot as plt
from sklearn.utils import check_random_state
from src.LinearRegression import *

from sklearn.datasets.samples_generator import make_regression 


x, y = make_regression(n_samples=100, n_features=1, n_informative=1,
                        random_state=0, noise=35) 
xx = [];
yy = []
for i in range(0, len(x)):
    xx.append(x[i, 0])
    yy.append(y[i])


print ('x.shape = %s y.shape = %s' % (len(xx), len(yy)))

lr = LinearRegression(0.06, xx, yy);
lr.train();

# Plot outputs
plt.scatter(xx, yy, color='black')

yyy = [];
xxx = [];
for i in xx:
    # if(i%3==0):
     yyy.append(lr.estimate(i))
     xxx.append(i)
    
plt.scatter(xxx, yyy, color='blue')

plt.show()
