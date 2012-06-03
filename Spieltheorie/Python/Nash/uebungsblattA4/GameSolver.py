'''
Created on 02.06.2012

@author: stefan
'''
from LcpSolver import LcpSolver

class GameSolver(object):
    '''
    classdocs
    '''


    def __init__(self, outcomes):
        '''
        Constructor
        '''
        self.outcomes = outcomes
        
    def findNash(self):
        supps1 = self.getSupport(1)
        supps2 = self.getSupport(2)
        for supp1 in supps1:
            for supp2 in supps2:
                sol = self.solve(supp1,supp2)
                if len(sol) != 0:
                    print "Spieler 1:"
                    for s in supp1:
                        print "\t" + str(s) + " -> " + str(sol[len(self.outcomes[0])+2+s])
                    print "\tPayoff: " + str(sol[0])
                    print "Spieler 2:"
                    for s in supp2:
                        print "\t" + str(s) + " -> " + str(sol[1+s])
                    print "\tPayoff: " + str(sol[len(self.outcomes[0])+1])
                    print ""

                
    def solve(self,supp1,supp2):
        lcpSolver = LcpSolver()
        
        for s1 in range(len(self.outcomes)):
            rel = 0 if s1 in supp1 else 1
            lhs = []
            lhs.append(1)
            for s2 in range(len(self.outcomes[0])):
                lhs.append(-self.outcomes[s1][s2][0])
            for s2 in range(len(self.outcomes)+1):
                lhs.append(0)
            lcpSolver.addConstraint(lhs, rel, 0)
            #print lhs
            ''' l.addConstraint([   1,      -4,       0,        0,     0,      0,      0], 0, 0) # SP1 spielt B '''
            ''' l.addConstraint([   1,      0,       -2,        -1,      0,      0,      0], 1, 0) # SP1 spielt S '''
                        
        for s1 in range(len(self.outcomes[0])):
            rel = 0 if s1 in supp2 else 1
            lhs = []
            for s2 in range(len(self.outcomes[0])+1):
                lhs.append(0)
            lhs.append(1)
            for s2 in range(len(self.outcomes)):
                lhs.append(-self.outcomes[s2][s1][1])
            lcpSolver.addConstraint(lhs, rel, 0)
            #print lhs
            ''' l.addConstraint([   0,      0,        0,        0,      1,      -2,     0], 0, 0) # SP2 spielt B  '''
            ''' l.addConstraint([   0,      0,        0,        0,      1,      0,     -4], 1, 0) # SP2 spielt S  '''
            ''' l.addConstraint([   0,      0,        0,        0,      1,      -1,    -3], 1, 0) # SP2 spielt X  ''' 
         
        for s1 in range(len(self.outcomes[0])): 
            lhs = []
            lhs.append(0)
            rel = 0 # gleich
            for s2 in range(len(self.outcomes[0])):
                if s1 == s2:
                    lhs.append(1)
                    if s2 in supp2:
                        rel = 1 #groesser
                else:
                    lhs.append(0)
            for s2 in range(len(self.outcomes)+1):
                lhs.append(0)
            lcpSolver.addConstraint(lhs, rel,0)
        
        for s1 in range(len(self.outcomes)): 
            lhs = []
            lhs.append(0)
            rel = 0 # gleich
            for s2 in range(len(self.outcomes[0])+1):
                lhs.append(0)
            for s2 in range(len(self.outcomes)):
                if s1 == s2:
                    lhs.append(1)
                    if s2 in supp1:
                        rel = 1 #groesser
                else:
                    lhs.append(0)
            lcpSolver.addConstraint(lhs, rel,0)
            #''' l.addConstraint([   0,      1,        0,        0,      0,      0,      0], 1, 0)  ''' 
            #''' l.addConstraint([   0,      0,        1,        0,      0,      0,      0], 0, 0)  ''' 
            #''' l.addConstraint([   0,      0,        0,        1,      0,      0,      0], 0, 0)  ''' 
            
        
        lhs = []
        lhs.append(0)
        for s1 in range(len(self.outcomes[0])): 
            lhs.append(1)
        for s2 in range(len(self.outcomes)+1):
            lhs.append(0)
        lcpSolver.addConstraint(lhs,0,1)
        
        lhs = []        
        for s2 in range(len(self.outcomes[0])+1):
            lhs.append(0)
        lhs.append(0)
        for s1 in range(len(self.outcomes)): 
            lhs.append(1)
        lcpSolver.addConstraint(lhs,0,1)
        
        optfunc = []
        for s in range(len(self.outcomes)+len(self.outcomes[0])+2):
            optfunc.append(0)
        lcpSolver.setOptfunc(optfunc)
        
        sol = lcpSolver.solve()
        #print sol
        return sol[1]
            
                
    def getSupport(self, player):
        if player == 1:
            numOfStrategies = len(self.outcomes)
        else:
            numOfStrategies = len(self.outcomes[0])
        
        supps = []
        for i in range(1,pow(2,numOfStrategies)):
            curr_supp = []
            index = 0
            supp_bin = ("{0:0"+str(numOfStrategies)+"b}").format(i)
            #print supp_bin
            for c in supp_bin:
                if c == '1':
                    curr_supp.append(index)
                index += 1
            supps.append(curr_supp)
        
        return supps
                

def main():
    # Picknick
    gs = GameSolver([
                              [[0,0], [1,2], [1,3], [1,4], [1,5]],
                              [[2,1], [0,0], [2,3], [2,4], [2,5]],
                              [[3,1], [3,2], [0,0], [3,4], [3,5]],
                              [[4,1], [4,2], [4,3], [0,0], [4,5]],
                              [[5,1], [5,2], [5,3], [5,4], [0,0]],
                                   ])
    gs.findNash()
    
if __name__ == "__main__":
    main()
