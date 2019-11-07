"""
created by: Ritam Basu
created on:06/11/19
created for: assignment1.

"""

from math import *
L = [1,2,4,8,16,32,64]
X = 5
j = 0
i = 0
while j< len(L):
    if 2**X == L[j]:
        print ("at index",j)
        i=i+1
    j=j+1
if i==0:
    print(X,"this value is not found in the list of 2^x")
