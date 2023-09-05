Lower=100
upper=4000

for num in range(Lower,upper):
    order=len(str(num))
    sum=0
    temp=num
    while num>0:
        digit=num%10
        sum += digit**order
        num//=10
    if temp==sum:
        print(sum)
