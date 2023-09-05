""" In Chefland, a valid phone number consists of 
5
5 digits with no leading zeros.
For example,
98765,10000, and 71023 are valid phone numbers while 
04123,9231, and872310 are not.Chef went to a store and purchased 
N items, where the cost of each item is X.
Find whether the total bill is equivalent to a valid phone number. """

for _ in range(int(input())):
    N,X=map(int,input().split())
    Z= N * X
    if 9999< Z <100000:
        print("yes")
    else:
        print("no")
