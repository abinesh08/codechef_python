""" In the medieval age, there were 3 kingdoms A, B, and C. The army of these kingdom had N A , N B, and N Csoldiers respectively.You are given that an army with X soldiers can defeat an army with 
Y soldiers only if X>Y.An army is said to be dominant if it can defeat both the other armies combined. For example, kingdom 
C's army will be dominant only if >+N C>N A+N B.Determine whether any of the armies is dominant or not. """

# cook your dish here
for _ in range(int(input())):
    A,B,C=map(int,input().split())
    if (A>B+C) or(B>A+C) or (C>A+B):
        print("yes")
    else:
        print("no")
