

from regression import *

import numpy as np

'''
Created on Dec 1, 2016

@author: UnmeshVinchurkar
'''
print ("Hello World!");

emp1 = Employee("Zara", 2000)
emp1.displayEmployee();



X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]];
    
M = np.matrix('12 7 3; 5 5 6; 7 8 9');
N = np.matrix('5 8 1; 6 7 3; 4 5 9');

print(M-N);


# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)