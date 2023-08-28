""" There are N bikes and M cars on the road Each bike has 2 tyres.Each car has 4 tyres.
Find the total number of tyres on the road. """

for _ in range(int(input())):
    B,C=map(int,input().split())
    print((B * 2)+(C * 4))
    
