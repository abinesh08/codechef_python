""" It's the sale season again and Chef bought items worth a total of 
X rupees. The sale season offer is as follows:if X≤100, no discount.
if 100<X≤1000, discount is 25 rupees.
if 1000<X≤5000, discount is 100 rupees.
if X>5000, discount is 500 rupees.Find the final amount Chef needs to pay for his shopping. """

for _ in range(int(input())):
    x=int(input())
    if x <=100:
        print(x)
    elif 100 < x <=1000:
        print(x - 25)
    elif 1000 < x <= 5000:
        print(x-100)
    else:
        print(x-500)
