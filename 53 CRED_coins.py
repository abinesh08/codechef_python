""" 
For each bill you pay using CRED, you earn 
X CRED coins.
At CodeChef store, each bag is worth 100 CRED coins.
Chef pays 
Y number of bills using CRED. Find the maximum number of bags he can get from the CodeChef store."""

for _ in range(int(input())):
    x,y=map(int,input().split())
    total_coins=x*y 
    print(total_coins//100)
