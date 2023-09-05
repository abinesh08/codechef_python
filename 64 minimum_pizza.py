""" Each pizza consists of 
4 slices. There are 
N friends and each friend needs exactly X slices.Find the minimum number of pizzas they should order to satisfy their appetite.  """

for _ in range(int(input())):
    a,b=map(int,input().split())
    
    c=(a*b)//4
    if ((a * b)%4==0):
        print(c)
    else:
        print(c+1)
