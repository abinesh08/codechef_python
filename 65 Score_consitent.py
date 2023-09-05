""" Chef is watching a football match. The current score is A:B, that is, team 1 has scored 
A goals and team 2 has scored 
B goals. Chef wonders if it is possible for the score to become C:D at a later point in the game (i.e. team 
1 has scored C goals and team 2 has scored D goals). Can you help Chef by answering his question? """

for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if (a==1) or (b==1) or (c==1) or (d==1):
        print("OUT")
    else:
        print("IN")
    
    
