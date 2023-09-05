num=int(input('Enter the three digit number:'))
sum=0

temp=num
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10

if temp==sum:
    print('amstrong nummber')
else:
    print('not a amstrong number')
    
#working
#153=1*1*1+5*5*5*+3*3*3=153(amstrong num)
#temp= num.......check num greater than 0
#create digit=num%10 example 153%10=3(remainder)
#sum=sum+3*3*3*......sum=0+27
#thn 15.2 is there using num//=10.....num=15.2//10=15
#then agin starting from first 15%10.......

num=int(input('Enter the number'))
temp=num
sum=0
length=len(str(num))
while num>0:
    digit=num%10
    sum+=digit**length
    num//=10

if temp==sum:
    print("the amstrong number:",)
else:
    print("not a amstrong")

