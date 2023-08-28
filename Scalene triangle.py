""" Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.
Note:
A triangle is said to be scalene if all three sides of the triangle are distinct.
It is guaranteed that the sides represent a valid triangle. """

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x==y or y==z or x==z:
        print("No")
    else:
        print("YES")
            
        
