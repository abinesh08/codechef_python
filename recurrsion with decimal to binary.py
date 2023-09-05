def converttobinary(n):
    if n<=1:
        converttobinary(n//2)
        print(n%2,end='')
num=int(input('enter the number:'))
converttobinary(num)
print()    
