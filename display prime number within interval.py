lower=int(input("Enter the lower number"))
higher=int(input("Enter the higher number"))
print("The interval between lower and higher")
for num in range(lower,higher):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)

lower=100
higher=200
print("the prime number between",lower, "and",higher, 'are:')
for num in range(lower,higher):
    if (num>1):
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)


