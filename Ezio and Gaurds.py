"""Ezio can manipulate at most 
X number of guards with the apple of eden.
Given that there are 
Y number of guards, predict if he can safely manipulate all of them."""

for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>=y:
        print("YES")
    else:
        print("NO")
