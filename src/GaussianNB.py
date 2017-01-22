'''
Created on Dec 4, 2016

@author: UnmeshVinchurkar
'''

import numpy as np
class LinearRegression():
    
    def __init__(self, alpha, xPoints, yPoints):
       self.alpha = alpha;  ''' learning rate'''        
       self.xPoints = xPoints
       self.yPoints = yPoints;
       self.mean = 0;
       self.sigma2 = 0;
