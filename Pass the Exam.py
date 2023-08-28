""" Chef appeared for an exam consisting of 3
3 sections. Each section is worth 
100 marks.

Chef scored A marks in Section 1
B marks in section 2 and 
C marks in section 3.

Chef passes the exam if both of the following conditions satisfy:

Total score of Chef is≥100;
Score of each section ≥10.
Determine whether Chef passes the exam or not. """


for _ in range(int(input())):
    x,y,z=map(int,input().split())
    total=x+y+z
    if x+y+z>=100 and x>=10 and y>=10 and z>=10:
        print("PASS")
    else:
        print("FAIL")
