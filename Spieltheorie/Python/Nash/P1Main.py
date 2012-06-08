
from uebungsblattP1.NfgReader import NfgReader
from uebungsblattP1.TwoPlayerStrategicGame import TwoPlayerStrategicGame
import sys
import time

def main():
    gamefile = sys.argv[1] 
    game = NfgReader().read(filename = gamefile)
    print game.game_title
    startTime = time.time()
    if isinstance(game, TwoPlayerStrategicGame):
        print "Time: " + str(time.time() - startTime) + " ", game.findMixedNash(oneNash = False)
    else:
        print "Time: " + str(time.time() - startTime) + " ", game.findPureNash()
        
    
if __name__ == "__main__":
    main()