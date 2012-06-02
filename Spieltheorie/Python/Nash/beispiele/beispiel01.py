'''
Created on 24.05.2012

@author: stefan
'''

from lp_solve import * 

f=[30,40]
A=[[25,75],[60,60],[68,34]]
b=[450,480,476]
x= lp_solve(f,A,b,[1,1,1],None, None, None, 1, 0)
print x