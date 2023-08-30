""" Chef has finally got the chance of his lifetime to drive in the 1
F1 tournament. But, there is one problem. Chef did not know about the 107% rule and now he is worried whether he will be allowed to race in the main event or not.
Given the fastest finish time as 
X seconds and Chef's finish time as 
Y seconds, determine whether Chef will be allowed to race in the main event or not.Note that, Chef will only be allowed to race if his finish time is within 107% of the fastest 
finish time. """

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=107/100
    if a*x>=y:
        print("YES")
    else:
        print("No")
