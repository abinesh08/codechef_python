#code18
""" Chef defines a group of three friends as a perfect group if the age of one person is equal to the sum of the age of remaining two people.

Given that, the ages of three people in a group are 
�
,
�
,
A,B, and 
�
C respectively, find whether the group is perfect.  """

for _ in range(int(input())):
    A,B,C=map(int,input().split())
    if (A+B==C) or (B+C==A) or (A+C==B):
        print("YES")
    else:
        print("NO")
