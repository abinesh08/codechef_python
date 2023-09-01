""" Janmansh received X coins of 10 rupees and Y coins of 5 rupees from Chingari. Since he is weak in math, can you find out how much total money does he have? """
for _ in range(int(input())):
    x,y= map(int,input().split())
    a= 10 * x
    b=5* y
    print(a+b)
