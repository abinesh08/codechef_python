""" Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained a monopolistic advantage in the market.
There are exactly 
3 companies in the market each of whose revenues are denoted by R 1, R 2and R 3respectively. A company is said to have a monopolistic advantage if its revenue is strictly greater than the sum of the revenues of its competitors.
Given the revenue of the 3 companies, help Chef determine if any of them has a monopolistic advantage. """

for _ in range(int(input())):
   R1,R2,R3= map(int,input().split())
   if (R1>R2+R3) or (R2>R1+R3) or (R3>R1+R2):
       print("Yes")
   else:
       print("No")
   
