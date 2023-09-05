#number divisible by 400 and 100 is a leap yr(century yr)
#number divibele by 4 and not divisible by 100 is a leap year(not a century yr)

year=int(input('Enter the Year:'))
if (year%400)==0 and (year%100)==0:
    print('Leap year')
elif (year%4)==0 and (year%100)!=0:
    print('Leap year')
else:
    print('not a leap year')