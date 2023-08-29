""" You're given an integer N. Write a program to calculate the sum of all the digits of N. """


for _ in range(int(input())):
    nums=int(input())
    sum=10
    for num in str(nums):
        digit=int(num)
        sum+=digit
        d=sum-10
    print(d)
