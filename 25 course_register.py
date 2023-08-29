""" There is a group of 
N friends who wish to enroll in a course together. The course has a maximum capacity of 
M students that can register for it. If there are K other students who have already enrolled in the course, determine if it will still be possible for all the N friends to do so or not.  """

for _ in range(int(input())):
    x,y,z= map(int,input().split())
    enrolled=x+z
    if enrolled <= y:
        print("YES")
    else:
        print("NO")

