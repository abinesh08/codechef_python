""" Chef has 3 numbers A,B and C.Chef wonders if it is possible to choose exactly two numbers out of the three numbers such that their sum is odd. """

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if ((x+y)%2!=0) or ((y+z)%2!=0) or ((x+z)%2!=0):
        print("yes")
    else:
        print("no")
