""" There are 
N children and Chef wants to give them 
1 candy each. Chef already has
X candies with him. To buy the rest, he visits a candy shop. In the shop, packets containing exactly 
4 candies are available.
Determine the minimum number of candy packets Chef must buy so that he is able to give 1 candy to each of the 
N children. """

from math import ceil
for _ in range(int(input())):
    n,c=map(int,input().split())
    if c >=n:
        print("0")
    else:
        print(ceil((n-c)/4))
