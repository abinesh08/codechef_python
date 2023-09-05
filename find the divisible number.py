my_list=[2,3,4,55,66,77,76,666,776,669]
my_result=list(filter(lambda x: (x%2==0),my_list))
print("The divisible are",my_result)

my_list=[2,3,5,6,7,99,888]
my_result=list(filter(lambda x: (x%2==0),my_list))
print('divisble by :',my_result)

#anonyms method
#(filter or map....(lambda x:(condtion),))