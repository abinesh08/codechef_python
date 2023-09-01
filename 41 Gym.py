""" Chef has decided to join a Gym in ChefLand and if possible, also hire a personal trainer at the gym. The monthly cost of the gym is 
X and personal training will cost him an additional Y per month. Chef's total budget per month is only 
Z. Print 1 if Chef can only join the gym, 2 if he can also have a personal trainer, and 0 if he can't even join the gym.
Note that if Chef wants to hire a personal trainer, he must join the gym — he cannot hire the trainer without joining the gym. """

for _ in range(int(input())):
    X,Y,Z=map(int,input().split())
    if X>Z:
        print("0")
    elif X+Y<=Z:
        print("2")
    elif X <=Z:
        print("1")
