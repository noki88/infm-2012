'''
Created on 03.06.2012

@author: stefan
'''
from TwoPlayerStrategicGame import TwoPlayerStrategicGame
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetPayoffMatrix(self):
        game_title = "Test Game"
        player_names = ["Sp1", "Sp2"]
        strategies = [["S11", "S12"],["S21", "S22"]]
        payoffs = [[1,1], [2,2], [3,3], [4,4]]
        outcomes = [1,2,3,4]
        game = TwoPlayerStrategicGame(game_title, player_names, strategies, payoffs, outcomes)
        self.assertEquals([[[1,1], [2,2]], [[3,3], [4,4]]], game.getPayoffMatrix())
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetPayoffMatrix']
    unittest.main()