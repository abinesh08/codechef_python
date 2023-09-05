""" Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

You are given three integers - B 1,B 2, and B 3 If B 1=1, it means that the first bottle is full.
If B 1 =0, it means that the first bottle is empty.Similarly, 
B 2denotes whether the second bottle is full or empty, and B 3
​denotes it for the third bottle.Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now". """


for _ in range(int(input())):
    b1,b2,b3=map(int,input().split())
    if (b1==0) and (b2==0):
        print("Water filling time")
    elif (b2==0) and (b3==0):
        print("Water filling time")
    elif (b1==0) and (b3==0):
        print("Water filling time")
    else:
        print("Not now")
