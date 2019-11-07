"""
created by: Ritam Basu
created on:06/11/19
created for: assignment1.

"""

from math import *
L = [1,2,4,8,16,32,64]
X = 5
j = 0
for i in range(len(L)):
    if 2**X == L[i]:
        s=L[i]
        j = j+1
       
if j==1:
    print ("index no.=",L.index(s))
else:
    print ("2^",X,"is not found in the given list")
