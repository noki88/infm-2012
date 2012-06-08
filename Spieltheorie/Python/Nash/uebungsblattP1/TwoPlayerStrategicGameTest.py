'''
Created on 03.06.2012

@author: stefan
'''

from NfgReader import NfgReader
from TwoPlayerStrategicGame import TwoPlayerStrategicGame
import os
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetPayoffMatrix1(self):
        game_title = "Test Game"
        player_names = ["Sp1", "Sp2"]
        strategies = [["S11", "S12"],["S21", "S22"]]
        payoffs = [["", 1,1], ["", 2,2], ["", 3,3], ["", 4,4]]
        outcomes = [1,2,3,4]
        game = TwoPlayerStrategicGame(game_title, player_names, strategies, payoffs, outcomes)
        self.assertEquals([[[1,1], [3,3]], [[2,2], [4,4]]], game.getPayoffMatrix())     
        
    def testGetPayoffMatrixFromFile(self):
        games = {
                 'bosx.nfg' :
                        [[[4, 2], [0, 0], [0, 1]], 
                         [[0, 0], [2, 4], [1, 3]]], 
                 
                 'sspes.nfg' :
                        [[[0, 0], [-1, 1], [1, -1], [1, -1], [-1, 1]], 
                         [[1, -1], [0, 0], [-1, 1], [1, -1], [-1, 1]], 
                         [[-1, 1], [1, -1], [0, 0], [-1, 1], [1, -1]], 
                         [[-1, 1], [-1, 1], [1, -1], [0, 0], [1, -1]], 
                         [[1, -1], [1, -1], [-1, 1], [-1, 1], [0, 0]]],
                 
                 'airstrike4.nfg' : 
                        [[[0, 0], [2, -2], [2, -2], [2, -2]], 
                         [[3, -3], [0, 0], [3, -3], [3, -3]], 
                         [[4, -4], [4, -4], [0, 0], [4, -4]], 
                         [[5, -5], [5, -5], [5, -5], [0, 0]]], 
                 
                 'bos.nfg' : 
                        [[[2, 1], [0, 0]], 
                         [[0, 0], [1, 2]]], 
                 
                 'sspb.nfg' : 
                        [[[0, 0], [-1, 1], [1, -1], [-1, 1]], 
                         [[1, -1], [0, 0], [-1, 1], [-1, 1]], 
                         [[-1, 1], [1, -1], [0, 0], [1, -1]], 
                         [[1, -1], [1, -1], [-1, 1], [0, 0]]], 
                 
                 'chicken.nfg' :
                        [[[3, 3], [2, 4]], 
                         [[4, 2], [1, 1]]], 
                 
                 'coordination.nfg' : 
                        [[[3, 3], [0, 0]], 
                         [[0, 0], [1, 1]]],
                 
                 'airstrike.nfg' : 
                        [[[0, 0], [2, -2], [2, -2]], 
                         [[3, -3], [0, 0], [3, -3]], 
                         [[4, -4], [4, -4], [0, 0]]]

                 }

        for (filename, payoffMatrix) in games.iteritems():
            game = NfgReader().read(filename="../games/" + filename)
            self.assertEquals(payoffMatrix, game.getPayoffMatrix())
        
    def testFindPureNash(self):
        pass
        game_title = "Test Game"
        player_names = ["Sp1", "Sp2"]
        strategies = [["S11", "S12"],["S21", "S22"]]
        payoffs = [["", 1,1], ["", 3,3]]
        outcomes = [2,1,1,2]
        game = TwoPlayerStrategicGame(game_title, player_names, strategies, payoffs, outcomes)
        self.assertEquals([[0,0],[1,1]], game.findPureNash())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetPayoffMatrix']
    unittest.main()