""" A problem setter is called an expert if at least 
50% of their problems are approved by Chef.
Munchy submitted X problems for approval. If 
Y problems out of those were approved, find whether Munchy is an expert or not. """

for _ in range(int(input())):
    x,y=map(int,input().split())
    z=x/2
    if y >= z:
        print("yes")
    else:
        print("no")
