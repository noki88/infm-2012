'''
Created on 02.06.2012
'''

class TwoPlayerStrategicGame(object):

    def __init__(self, game_title, player_names, strategies, payoffs, outcomes):
        self.game_title = game_title
        self.player_names = player_names
        self.strategies = strategies
        self.payoffs = payoffs
        self.outcomes = outcomes
        
    def __str__(self):
        s = ""
        s += "Game Title: " + self.game_title.__str__()
        s += "\nPlayer Names: " + self.player_names.__str__()
        s += "\nStrategies: " + self.strategies.__str__()
        s += "\nPayoffs: " + self.payoffs.__str__()
        s += "\nOutcomes: " + self.outcomes.__str__()
        return s
    
    def getPayoffMatrix(self):
        matrix = []
        for i in range(len(self.strategies[0])):
            row = []
            for j in range(len(self.strategies[1])):
                row.append(self.payoffs[self.outcomes[i*len(self.strategies[1])+j]-1])
            matrix.append(row)
        return matrix
        