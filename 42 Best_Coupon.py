""" Chef is ordering food online (instead of cooking) and the bill comes out to be Rs. 
X. Chef can use one of the following two coupons to avail a discount.
Get 10 percent off on the bill amount
Get a flat discount of Rs. 100 on the bill amount
What is the maximum discount Chef can avail? """

for _ in range(int(input())):
    X= int(input())
    if X<=1000:
        print("100")
    else:
        print((X // 100) * 10)
