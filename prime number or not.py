

num=int(input("Enter the value"))
flag=0
if num>2:
    for i in range(2,num):
        if (num%i)==0:
            flag=1
    if (flag==1):
        print("not a prime number")
    else:
        print("Prime number")


a=int(input('Enter the number:'))
flag = 0
if a > 1:
    for i in range(2, a):
         if (a % i)==0:
             flag = 1
         break

    if flag == 1:
        print('not a prime')
    else:
        print('prime')



