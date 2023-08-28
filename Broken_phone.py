"""Uttu broke his phone. He can get it repaired by spending 
X rupees or he can buy a new phone by spending 
Y rupees. Uttu wants to spend as little money as possible. Find out if it is better to get the phone repaired or to buy a new phone."""

# cook your dish here
for _ in range(int(input())):
    repair,new=map(int,input().split())
    if repair < new:
        print("Repair")
    elif repair == new:
        print("any")
    else:
        print("New phone")
