""" Most programmers will tell you that one of the ways to improve your performance in competitive programming is to practice a lot of problems.

Our Chef took the above advice very seriously and decided to set a target for himself.

Chef decides to solve at least 10 problems every week for 4 weeks.Given the number of problems he actually solved in each week over 4 weeks as 1,2,3,P 1,P 2 ,P 3, and P 4,
output the number of weeks in which Chef met his target. """

A=(map(int,input().split()))
problems=0

for i in A:
    if i>=10:
        problems+=1
print(problems)
    
    
