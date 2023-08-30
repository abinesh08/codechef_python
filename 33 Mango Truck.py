""" You are given that a mango weighs 
X kilograms and a truck weighs 
Y kilograms. You want to cross a bridge that can withstand a weight of 
Z kilograms.Find the maximum number of mangoes you can load in the truck so that you can cross the bridge safely. """

for _ in range(int(input())):
    X,Y,Z= map(int,input().split())
    W= Z - Y 
    print(W//X)
