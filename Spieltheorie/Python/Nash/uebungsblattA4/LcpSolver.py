'''
Created on 02.06.2012

@author: stefan
'''

from lp_solve import * 

class LcpSolver(object):
    '''
    classdocs
    '''
    relations = {'<' : -1, 
                 '=' : 0, 
                 '>' : 1}


    def __init__(self):
        '''
        Constructor
        '''
        self.lhs = []
        self.rhs = []
        self.rel = []
        self.optfunc = []
        
    def addConstraint(self, lhs, rel, rhs):
        self.lhs.append(lhs)
        self.rel.append(rel)
        self.rhs.append(rhs)
        #print str(lhs) + " " + str(rel) + " " + str(rhs)
        
    def setOptfunc(self, optfunc):
        self.optfunc = optfunc
        
    def solve(self):
        return lp_solve(self.optfunc,self.lhs,self.rhs,self.rel,None, None, None, 1, 0)
        

    
        
        
        
    