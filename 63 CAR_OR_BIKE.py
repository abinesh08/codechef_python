""" Chef wants to reach home as soon as possible. He has two options:

Travel with his BIKE which takes 
X minutes.
Travel with his CAR which takes Y minutes.
Which of the two options is faster or do they both take same time? """

for _ in range(int(input())):
    a,b=map(int,input().split())
    if a > b :
        print("BIKE")
    elif a<b:
        print("CAR")
    else:
        print("SAME")
