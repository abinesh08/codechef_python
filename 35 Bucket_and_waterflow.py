""" Alice has a bucket of water initially having 
W litres of water in it. The maximum capacity of the bucket is 
X liters.
Alice turned on the tap and the water starts flowing into the bucket at a rate of 
Y litres/hour. She left the tap running for exactly 
Z hours. Determine whether the bucket has been overflown, filled exactly, or is still left unfilled.Input Format
The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
Each test case consists of a single line of input containing four space-separated integers
W, X, Y, Z. """

for _ in range(int(input())):
    I,C,F,H=map(int,input().split())
    TF=F * H 
    current= I + TF
    if C == current:
        print("filled")
    elif C < current:
        print("overflow")
    else:
        print("not filled")
