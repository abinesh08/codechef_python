num=int(input('Enter the number'))
sum=0
if num<0:
    print('give a positive numbers:')
else:
   for i in range(1,num):
       sum+=i
       print(sum)