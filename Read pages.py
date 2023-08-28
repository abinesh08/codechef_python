""" Chef has started studying for the upcoming test. The textbook has 
�
N pages in total. Chef wants to read at most 
�
X pages a day for 
�
Y days.

Find out whether it is possible for Chef to complete the whole book. """


for _ in range(int(input())):
    A,B,C=map(int,input().split())
    if (B*C)>=A:
        print("Yes")
    else:
        print("No")
