""" Summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

Rent a cooler at the cost of X coins per month.
Purchase a cooler for Y coins.
Given that the summer season will last for M months in Chefland, help Chef in finding whether he should rent the cooler or not.
Chef rents the cooler only if the cost of renting the cooler is strictly less than the cost of purchasing it. Otherwise, he purchases the cooler.
Print YES if Chef should rent the cooler, otherwise print NO. """

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    t= x*z 
    if t<y:
        print("yes")
    else:
        print("no")
