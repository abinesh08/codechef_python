""" Janmansh has to submit 
3 assignments for Chingari before 
10 pm and he starts to do the assignments at 
X pm. Each assignment takes him 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not? """

for _ in range(int(input())):
    x= int(input())
    y=x+3
    if 10 >= y:
        print("yes")
    else:
        print("no")
    
