"""Chef is looking to buy a TV and has shortlisted two models. The first one costs 
A rupees, while the second one costs B rupees.
Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of 
C rupees on the first TV, and a flat discount of D rupees on the second one.

Help Chef determine which of the two TVs would be cheaper to buy during the sale."""

# cook your dish here
for _ in range(int(input())):
    A,B,C,D=map(int,input().split())
    A_discount= A - C 
    B_discount= B - D
    if A_discount < B_discount:
        print("First")
    elif A_discount == B_discount:
        print("Any")
    else:
        print("Second")
