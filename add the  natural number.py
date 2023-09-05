def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)
num=int(input('enter the value: '))
if num>=1:
    print(recur_sum(num))

