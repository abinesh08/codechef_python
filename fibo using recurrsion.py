def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n-1)) + (recur_fibo(n-2))
nterms=int(input('enter the fibo: '))
print('the fibo series are:')
if nterms<=1:
         print('enter the positive and more thn 1')
else:
        for i in range(nterms):
            print(recur_fibo(i))


    


