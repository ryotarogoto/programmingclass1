'''
Created on 2013/05/07

@author: dmn1003
'''
import random
na = ["A", "T", "C", "G"]

class SimpleDNA:
    
    def __init__(self, numArray):
        self.a = list()
        for i in range(numArray):
            self.a.append(na[random.randint(0,3)])
            
    def printDNA(self):
        print self.a
        
    def getDNA(self):
            return self.a
        
        

    
