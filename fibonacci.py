#fiboacci: 0,1,1,2,3,5

nterms=int(input('enter the number:'))
n1,n2=0,1
count=0
#check the number is positive or negative or 1
if nterms<count:
    print('enter the postive number:')
elif nterms==1:
    print(n1)
else:

    print('Fibonacci series are:')
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

        