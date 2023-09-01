""" There is a cricket match in Chefland. Chef's team requires N runs to win in M overs.
Given that 
1 over consists of6 balls and a player can score a maximum of 6 runs in a ball, find whether Chef's team can win. """

for  _ in range(int(input())):
    N,M=map(int,input().split())
    maximum=M *36
    if N > maximum:
        print("no")
    else:
        print("yes")
