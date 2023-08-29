""" Chef owns a car that can run 15 kilometers using 1 liter of petrol.
He wants to attend a programming camp at DAIICT.
X liters of petrol is present in Chef's car. The distance between his house and DAIICT is Y kilometers.
Determine whether Chef can attend the event and return to his home with the given amount of petrol.
Note: Chef has to return back to home, so the total distance to be covered would be 2⋅Y. """

for _ in range(int(input())):
    l,k=map(int,input().split())
    litres= l*15
    kilometers=k*2
    if litres>=kilometers:
        print("YES")
    else:
        print("No")
