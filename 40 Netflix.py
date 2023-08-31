""" Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two users to share a subscription.
Given that Alice, Bob, and Charlie have 
A,B, and C rupees respectively and a Netflix subscription costs X rupees, find whether any two of them can contribute to buy a subscription. """

for _ in range(int(input())):
    A,B,C,X=map(int,input().split())
    if (A+B>=X) or (B+C>=X) or (C+A>=X):
        print("YES")
    else:
        print("No")
