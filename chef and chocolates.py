""" Chef has 
�
X 5 rupee coins and 
�
Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs 
�
Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina."""

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    tc= (5*x) + (10*y)
    print(tc // z)


