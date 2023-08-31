""" Chef wants to gift 
C chocolates to Botswal on his birthday. However, he has only X chocolates with him.The cost of 1 chocolate is Y rupees.
Find the minimum money in rupees Chef needs to spend so that he can gift 
C chocolates to Botswal. """

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    N= a-b
    buy=N * c
    print(buy)
    
#N= need chocolates
#buy= amount
