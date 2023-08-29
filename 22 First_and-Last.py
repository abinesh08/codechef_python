""" Given an integer N . Write a program to obtain the sum of the first and last digits of this number. """

for i in range(int(input())):
    s = input()
    print(int(s[0]) + int(s[-1]))
