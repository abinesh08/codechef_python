def recur_factorial(n):
    if n==1:
        return n
    else:
        return n * (recur_factorial(n-1))
num=int(input('enter the value:'))
if num<=1:
    print('give pv num:')
else:
    print(recur_factorial(num))