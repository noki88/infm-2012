'''
Created on 02.06.2012

@author: stefan
'''
from GameSolver import GameSolver
import unittest


class Test(unittest.TestCase):


    def testSupport(self):
        gs = GameSolver([
                                    [[4,2], [0,0], [0,1]],
                                    [[0,0], [2,4], [1,3]]
                                   ])

        self.assertEquals([[1], [0], [0, 1]], gs.getSupport(1))
        self.assertEquals([[2], [1], [1, 2], [0], [0, 2], [0, 1], [0, 1, 2]], gs.getSupport(2))
        
    def testSolveGame(self):
        gs = GameSolver([
                              [[4,2], [0,0], [0,1]],
                              [[0,0], [2,4], [1,3]]
                                   ])

        for supp1 in gs.getSupport(1):
            for supp2 in gs.getSupport(2):
                #print supp1
                #print supp2
                gs.solve(supp1, supp2)
                #print ""
                
    def testFindNash1(self):
        gs = GameSolver([
                              [[4,2], [0,0], [0,1]],
                              [[0,0], [2,4], [1,3]]
                                   ])
        print gs.findNash()
        
    def testFindNash2(self):
        gs = GameSolver([
                              [[0,0], [1,2], [1,3], [1,4], [1,5]],
                              [[2,1], [0,0], [2,3], [2,4], [2,5]],
                              [[3,1], [3,2], [0,0], [3,4], [3,5]],
                              [[4,1], [4,2], [4,3], [0,0], [4,5]],
                              [[5,1], [5,2], [5,3], [5,4], [0,0]],
                                   ])
        print gs.findNash()
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSupport']
    unittest.main()