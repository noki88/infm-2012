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
        

def main():
    l = LcpSolver()
    ''' (B,S) vs. (B,S,X) '''
    '''                 u,      b(B),     b(S),    b(X),     v,     a(B),    a(S) '''
    l.addConstraint([   1,      -4,       0,        0,     0,      0,      0], 0, 0) # SP1 spielt B 
    l.addConstraint([   1,      0,       -2,        -1,      0,      0,      0], 1, 0) # SP1 spielt S 
    l.addConstraint([   0,      0,        0,        0,      1,      -2,     0], 0, 0) # SP2 spielt B 
    l.addConstraint([   0,      0,        0,        0,      1,      0,     -4], 1, 0) # SP2 spielt S 
    l.addConstraint([   0,      0,        0,        0,      1,      -1,    -3], 1, 0) # SP2 spielt X 
    l.addConstraint([   0,      1,        0,        0,      0,      0,      0], 1, 0)
    l.addConstraint([   0,      0,        1,        0,      0,      0,      0], 0, 0)
    l.addConstraint([   0,      0,        0,        1,      0,      0,      0], 0, 0)
    l.addConstraint([   0,      0,        0,        0,      0,      1,      0], 1, 0)
    l.addConstraint([   0,      0,        0,        0,      0,      0,      1], 0, 0)
    l.addConstraint([   0,      1,        1,        1,      0,      0,      0], 0, 1)
    l.addConstraint([   0,      0,        0,        0,      0,      1,      1], 0, 1)
    l.setOptfunc([      0,      0,        0,        0,      0,      0,      0])
    x = l.solve()
    print x
    
if __name__ == "__main__":
    main()
    
        
        
        
    