""" Chef has opened a new airline. Chef has 10 airplanes where each airplane has a capacity of 
X passengers.On the first day itself, 
Y people are willing to book a seat in any one of Chef's airplanes.Given that Chef charges Z rupees for each ticket, find the maximum amount he can earn on the first day. """


for _ in range(int(input())):
    A,B,C=map(int,input().split())
    Seats= 10*A 
    if Seats >= B:
        print(B*C)
    else:
        print(Seats*C)
