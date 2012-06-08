'''
Created on 02.06.2012
'''
from uebungsblattA4.GameSolver import GameSolver

class TwoPlayerStrategicGame(object):

    def __init__(self, game_title, player_names, strategies, payoffs, outcomes):
        self.game_title = game_title
        self.player_names = player_names
        self.strategies = strategies
        self.payoffs = payoffs
        self.outcomes = outcomes
        self.payoffs = []
        self.payoffs.append(list(["draw"]+([0]*len(self.player_names))))
        self.payoffs += payoffs
        for payoff in self.payoffs:
            del payoff[0]
        #print self.payoffs
        self.payoff_matrix = self.getPayoffMatrix()
        #print self.getPayoffMatrix()
        
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
            matrix.append([])
            
        for j in range(len(self.strategies[1])):
            for i in range(len(self.strategies[0])):
                matrix[i].append(self.payoffs[self.outcomes[j*len(self.strategies[0])+i]])
                #print str(self.outcomes[j*len(self.strategies[0])+i])
        return matrix

    def findPureNash(self):
        nash = []
        # find best answers for player 1 for strategies of player 2
        for s2 in range(0,len(self.payoff_matrix[0])):
            for s1 in range(0,len(self.payoff_matrix)):
                cur_payoff = self.payoff_matrix[s1][s2]
                isNash = True
                for s11 in range(0,len(self.payoff_matrix)):
                    if self.payoff_matrix[s11][s2][0] > cur_payoff[0]:
                        isNash = False
                for s21 in range(0,len(self.payoff_matrix[0])):
                    if self.payoff_matrix[s1][s21][1] > cur_payoff[1]:
                        isNash = False
                if isNash:
                    #print cur_payoff
                    nash.append([s1,s2])
        return nash
    
    def findMixedNash(self, oneNash = False):
        #print "\n",self.getPayoffMatrix()
        solver = GameSolver(self.getPayoffMatrix())
        #print solver.findNash(oneNash)
        return solver.findNash(oneNash)