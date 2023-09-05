def compute_factors(x):
    
    for i in range(1,num+1):
        if num%i==0:
            print(i)
           
num=int(input('Enter the number:'))
compute_factors(num)
