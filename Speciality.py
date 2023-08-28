"""On every CodeChef user's profile page, the list of problems that they have set, tested, and written editorials for, is listed at the bottom.

Given the number of problems in each of these 3 categories as X,Y, and 
Z respectively (where all three integers are distinct), find if the user has been most active as a Setter, Tester, or Editorialist."""

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if (x>y) and (x>z):
        print("setter")
    elif (y>x) and (y>z):
        print("tester")
    else:
        print("Editorialist")
    
