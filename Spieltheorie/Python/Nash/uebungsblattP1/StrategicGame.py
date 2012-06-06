'''
Created on 02.06.2012
'''


from timeit import itertools
import sys

class StrategicGame(object):

    def __init__(self, game_title, player_names, strategies, payoffs, outcomes):
        self.game_title = game_title
        self.player_names = player_names
        self.strategies = strategies
        self.payoffs = payoffs
        self.outcomes = outcomes
        self.payoffs.insert(0, ["draw"]+([0]*len(self.player_names)))
        tmp = self.strategies
        tmp.reverse()
        strategy_profiles = list(itertools.product(*tmp))
        self.strategy_profiles = []
        for (x,y,i) in zip(strategy_profiles, self.outcomes, range(len(strategy_profiles))):
            x = list(x)
            x.reverse()
            self.strategy_profiles.append(x)
            #print "",i,"profile",x,"outcome",y
            
        
    def __str__(self):
        s = ""
        s += "Game Title: " + self.game_title.__str__()
        s += "\nPlayer Names: " + self.player_names.__str__()
        s += "\nStrategies: " + self.strategies.__str__()
        s += "\nPayoffs: " + self.payoffs.__str__()
        s += "\nOutcomes: " + self.outcomes.__str__()
        s += "\nStrategy Profiles: " + self.strategy_profiles.__str__()
        return s
        
    def findPureNash(self):
        nash = []
        bestAnswers = []
        #print self.strategy_profiles
        for players in range(0,len(self.player_names)):
            strategiesOfOtherPlayers = []
            for strategie in range(0,len(self.strategies)):
                if strategie != players:
                    strategiesOfOtherPlayers.append(self.strategies[strategie])
            currentPlayersBestAnswers = []
            for othersStrategies in list(itertools.product(*strategiesOfOtherPlayers)):
                currentBestAnswers = []               
                bestPayoff = -sys.maxint - 1
                for strategyOfCurrentPlayer in self.strategies[players]:
                    currentProfile = []
                    currentProfile += othersStrategies
                    currentProfile.insert(players, strategyOfCurrentPlayer)
                    #print currentProfile
                    indexInAllProfiles = list(self.strategy_profiles).index(currentProfile)
                    currentPayoff = self.payoffs[self.outcomes[indexInAllProfiles]][players+1]
                    if currentPayoff > bestPayoff:
                        currentBestAnswers = [tuple(currentProfile)]
                        bestPayoff = currentPayoff
                    elif currentPayoff == bestPayoff:
                        currentBestAnswers.append(tuple(currentProfile))
                #print "player " + str(players) + ": best answer for " + str(othersStrategies) + " is " + str(bestAnswers)
                #bestAnswers.append(tuple(currentBestAnswers))
                currentPlayersBestAnswers += currentBestAnswers
            bestAnswers.append(currentPlayersBestAnswers)
                
        nash = set(tuple(bestAnswers[0]))
        for players in range(len(self.player_names)):
            nash = nash & set(tuple(bestAnswers[players]))

        return nash


