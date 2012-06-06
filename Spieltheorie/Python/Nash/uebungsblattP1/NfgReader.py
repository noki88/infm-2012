'''
Created on 02.06.2012
'''

from StrategicGame import StrategicGame
from TwoPlayerStrategicGame import TwoPlayerStrategicGame
import os
import re
import time

class NfgReader(object):
    
    def read(self, filename):
        f = open(filename, 'r')
        s = f.read()
        game_title = re.search('(?<=")\w+.*?(?=")', s).group(0)
        player_names = re.search('(?={).*?(?=})', s).group(0) + "}"
        player_names = player_names.replace('{', '[').replace('}', ']').replace('" "', '","')
        player_names = eval(player_names)
        strategies = re.findall('{.{.*?}.}',s,re.DOTALL)[0]
        strategies = strategies.replace('{', '[').replace('}', ']').replace('" "', '","').replace('\n', '').replace("][", "],[")
        strategies = eval(strategies)
        payoffs = re.findall('{.{.*?}.}',s,re.DOTALL)[1]
        payoffs = payoffs.replace('{', '[').replace('}', ']').replace('" "', '","').replace('\n', '').replace("][", "],[").replace('" ' , '",')
        payoffs = eval(payoffs)
        outcomes = re.search('(\d+\s)+(\d|\n)',s).group(0)
        outcomes = "[" + outcomes.replace(" ", ",") + "]"
        outcomes = eval(outcomes)
        if len(player_names) == 2:
            return TwoPlayerStrategicGame(game_title=game_title, player_names=player_names, strategies=strategies, payoffs=payoffs, outcomes=outcomes)
        else:
            return StrategicGame(game_title=game_title, player_names=player_names, strategies=strategies, payoffs=payoffs, outcomes=outcomes)

def main():
    games = os.listdir("../games/")
    games = ["airstrike.nfg"]
    for file in games:
        game = NfgReader().read(filename="../games/" + file)
        print game.game_title
        startTime = time.time()
        if isinstance(game, TwoPlayerStrategicGame):
            print "Time: " + str(time.time() - startTime) + " ", game.findMixedNash(oneNash = False)
        else:
            print "Time: " + str(time.time() - startTime) + " ", game.findPureNash()
        print "-----------------------------------------------------------"
        
    
if __name__ == "__main__":
    main()


