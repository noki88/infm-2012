'''
Created on 02.07.2012

@author: swrobel & vkurz
'''
from KemenyYoung import KemenyYoung
from pprint import pprint

def expand(pi):
    piExpanded = []
    for pii in pi:
        for i in range(pii.get('count')):
            piExpanded.append(tuple(pii.get('preference')))
    return piExpanded

def main():
    pi = [{'count':25, 'preference':['b', 'a', 'd', 'e', 'c']},
          {'count':12, 'preference':['e', 'd', 'c', 'b', 'a']},
          {'count':11, 'preference':['c', 'e', 'a', 'b', 'd']},
          {'count':14, 'preference':['d', 'a', 'b', 'e', 'c']},
          {'count':18, 'preference':['e', 'b', 'd', 'c', 'a']},
          {'count':10, 'preference':['c', 'd', 'a', 'e', 'b']},
          {'count':10, 'preference':['c', 'd', 'e', 'b', 'a']}]
    
    pprint(KemenyYoung.F(expand(pi)))

if __name__ == '__main__':
    main()
