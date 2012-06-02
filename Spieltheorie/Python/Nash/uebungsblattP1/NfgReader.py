'''
Created on 02.06.2012
'''

import re
from TwoPlayerStrategicGame import TwoPlayerStrategicGame

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
        payoffs = payoffs.replace('{', '[').replace('}', ']').replace('" "', '","').replace('\n', '').replace("][", "],[").replace('""', '"",')
        payoffs = eval(payoffs)
        outcomes = re.search('(\d\s)+\d',s).group(0)
        outcomes = "[" + outcomes.replace(" ", ",") + "]"
        outcomes = eval(outcomes)
        return TwoPlayerStrategicGame(game_title=game_title, player_names=player_names, strategies=strategies, payoffs=payoffs, outcomes=outcomes)
    
        
    
