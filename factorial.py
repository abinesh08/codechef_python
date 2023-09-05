#factorial=factorial*1
#eg 2!=1*2
#so use (1,num+1)

num=int(input('Enter the number:'))
#check the number is positive,ngeative or zero
if num<0:
    print('not exist')
elif num==0:
    print('factorial of 0 is 1')
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
        print(factorial)
