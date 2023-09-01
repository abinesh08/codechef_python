""" You are given 
3 numbers A,B, and C.Determine whether the average of A and B is strictly greater than C or not?
NOTE: Average of A and B is defined as (+)2(A+B). For example, average of 5 and 9 is 7, average of 5 and 8 is 6.5. """

for _ in range(int(input())):
    A,B,C=map(int,input().split())
    average= (A + B) / 2
    if average>C:
        print("yes")
    else:
        print("no")
