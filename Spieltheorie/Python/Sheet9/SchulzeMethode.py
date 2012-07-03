'''
Created on 02.07.2012

@author: swrobel & vkurz
'''
from pprint import pprint

class SchulzeMethode(object):

    @staticmethod
    def F(pi):
        pairwiseComparison = {}
        strongestPath = {}
        
        ''' init pairwise matrix / path matrix '''
        for candidate1 in pi[0]:
            pairwiseComparison[candidate1] = {}
            strongestPath[candidate1] = {}
            for candidate2 in pi[0]:
                pairwiseComparison[candidate1][candidate2] = 0
                strongestPath[candidate1][candidate2] = 0
        
        ''' pairwiseComparison '''
        for order in pi:
            for candidate1 in pi[0]:
                for candidate2 in pi[0]:
                    if order.index(candidate2) > order.index(candidate1):
                        pairwiseComparison[candidate1][candidate2] += 1
        
        ''' build graph '''
        for fromKey, fromValue in pairwiseComparison.items():
            for toKey, toValue in fromValue.items():
                if(fromKey != toKey):
                    if pairwiseComparison[fromKey][toKey] > pairwiseComparison[toKey][fromKey]:
                        strongestPath[fromKey][toKey] = pairwiseComparison[fromKey][toKey]
                    else:
                        # no strongestPath
                        strongestPath[fromKey][toKey] = 0
                        
        ''' search for the strongest path '''
        for viaCandidate in pi[0]:
            for fromCandidate in pi[0]:
                if(viaCandidate == fromCandidate):
                    continue
                for toCandidate in pi[0]:
                    if(viaCandidate !=  toCandidate and fromCandidate != toCandidate):
                        strongestPath[fromCandidate][toCandidate] = max(strongestPath[fromCandidate][toCandidate], min(strongestPath[fromCandidate][viaCandidate],strongestPath[viaCandidate][toCandidate]))
                        
        ''' look for potential winner '''
        potentialWinner = []
        for candidate1 in pi[0]:
            isPotentialWinner = True
            for candidate2 in pi[0]:  
                    if(strongestPath[candidate1][candidate2] < strongestPath[candidate2][candidate1]):
                        isPotentialWinner = False
                        break
            if(isPotentialWinner):
                potentialWinner.append(candidate1)
                    
        #pprint(pairwiseComparison) 
        #pprint(strongestPath)     
        #pprint(potentialWinner)
        
        return potentialWinner
        
        