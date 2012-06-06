'''
Created on 06.06.2012

@author: stefan
'''
from NfgReader import NfgReader
from TwoPlayerStrategicGame import TwoPlayerStrategicGame
import os
import time


def statistics():
    games = os.listdir("../games/")
    runs = 10
    games = ["bosx.nfg"]
    for file in games:
        game = NfgReader().read(filename="../games/" + file)
        print game.game_title
        
        print "Computing one NE with own algorithm...",
        alltime = 0
        for i in range(runs):
            startTime = time.time()
            game.findMixedNash(oneNash = True)
            alltime += time.time() - startTime
        print "Time: " + str(alltime/runs) + "\n", 
        
        print "Computing all NE with own algorithm...",
        alltime = 0
        for i in range(runs):
            startTime = time.time()
            game.findMixedNash(oneNash = False)
            alltime += time.time() - startTime
        print "Time: " + str(alltime/runs) + "\n"
        
        '''
        print "Computing one NE with gambit...",
        alltime = 0
        for i in range(runs):
            startTime = time.time()
            os.system("gambit-enummixed -S " + "< ../games/" + file)
            alltime += time.time() - startTime
        print "Time: " + str(alltime/runs) + "\n"
        '''
        
        print "Computing all NE with gambit...",
        alltime = 0
        for i in range(runs):
            startTime = time.time()
            os.system("gambit-enummixed -q -S " + "< ../games/" + file + " > /dev/null")
            alltime += time.time() - startTime
        print "Time: " + str(alltime/runs) + "\n"
        print "-----------------------------------------------------------"
        
if __name__ == '__main__':
    statistics()