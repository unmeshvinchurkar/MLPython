'''
Created on Dec 2, 2016

@author: UnmeshVinchurkar
'''
import numpy as np
class LinearRegression():
    
    def __init__(self, alpha, xPoints, yPoints):
       self.alpha = alpha;  ''' learning rate'''        
       self.xPoints = xPoints
       self.yPoints = yPoints;
       self.pMatrix = np.matrix('0.0; 0.0');
       
    def getParams(self):        
     return self.pMatrix;
       
    def estimate(self, x):        
       return self.pMatrix[0, 0] + x * self.pMatrix[1, 0]  
       
    def train(self):
           
        length = len(self.xPoints);           
        self.pMatrix = np.matrix('6.48;2.21; -124579.8;1.0');       
        
        oldCost = self.calCost(self.pMatrix);
        newCost = oldCost + 200;
        
        p0 = self.pMatrix[0, 0];
        p1 = self.pMatrix[1, 0];
       # p2 = self.pMatrix[2, 0];
       # p3 = self.pMatrix[3, 0];
        
        converged = False
        max_iter = 10000
        iter = 0
        
        # for i in range(0, 100):           
        while not converged:   
               
                 Dp0 = sum(((p0 + p1 * self.xPoints[j] - float(self.yPoints[j])) / float(length * 1.0)) for j in range(0, 100))
                 Dp1 = sum(((p0 + p1 * self.xPoints[j] - float(self.yPoints[j])) * self.xPoints[j] / float(length * 1.0)) for j in range(0, 100))
                 # Dp2 = sum(((p0 + p1 * self.xPoints[j] - float(self.yPoints[j])) * (self.xPoints[j]**2 )/ float(length * 1.0)) for j in range(0, 100))   
                # Dp3 = sum(((p0 + p1 * self.xPoints[j] - float(self.yPoints[j])) * (self.xPoints[j]**3 )/ float(length * 1.0)) for j in range(0, 100))   
                               
                   # update the theta_temp
                 temp0 = p0 - self.alpha * Dp0;
                 temp1 = p1 - self.alpha * Dp1;
                # temp2 = p2 - self.alpha * Dp2;
                 # temp3 = p3 - self.alpha * Dp3;
    
        # update theta
                 p0 = temp0
                 p1 = temp1  
                # p2 = temp2
                # p3 = temp3           
                    
                 self.pMatrix[0, 0] = p0
                 self.pMatrix[1, 0] = p1 
                # self.pMatrix[2, 0] = p2 
                # self.pMatrix[3, 0] = p3 
                 oldCost = newCost
                 newCost = self.calCost(self.pMatrix);
                 
                   # mean squared error
       

                 if abs(oldCost - newCost) <= 3:
                     print ('Converged, iterations: ', iter, '!!!')
                     converged = True
    
                 iter += 1  # update iter
    
                 if iter == max_iter:
                    print ('Max interactions exceeded!')
                    converged = True 
                    print('old cost ', oldCost)  
                    print('new cost ', newCost)        
                
      
              
     
     
    def calCost(self, pMatrix):              
        J = 0;
        length = len(self.xPoints);   
        
        for x in range(0, length):
            J = J + (pMatrix[0, 0] + self.xPoints[x] * pMatrix[1, 0] - self.yPoints[x]) ** 2 / (2.0 * length);           
        
        return J;  
           
           
           
       
       
        
        
