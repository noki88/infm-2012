'''
Created on 02.07.2012

@author: swrobel & vkurz
'''
#from pprint import pprint

class KemenyYoung(object):

    @staticmethod
    def F(pi):
        pairwiseComparison = {}
        
        ''' init pairwise matrix '''
        for candidate1 in pi[0]:
            pairwiseComparison[candidate1] = {}
            for candidate2 in pi[0]:
                pairwiseComparison[candidate1][candidate2] = 0
        
        ''' pairwiseComparison '''  
        for order in pi:
            for candidate1 in pi[0]:
                for candidate2 in pi[0]:
                    if order.index(candidate2) > order.index(candidate1):
                        pairwiseComparison[candidate1][candidate2] += 1
                        
        #pprint(pairwiseComparison)          
        
        sof = {}
        for order in pi:
            if sof.has_key(order):
                continue
            sof[order] = 0
            for j in range(0,len(order)-1):
                for k in range(j+1,len(order)):
                    sof[order] += pairwiseComparison[order[j]][order[k]]
                    
        #pprint(sof)
        
        return max([(value, key) for key, value in sof.items()])[1]

        
