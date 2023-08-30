""" Chef's phone shows a Battery Low notification if the battery level is 15% or less.Given that the battery level of Chef's phone is X%, determine whether it would show a Battery low 
notification. """

for _ in range(int(input())):
    Battery = int(input())
    if Battery <=15:
        print("yes")
    else:
        print("no")
