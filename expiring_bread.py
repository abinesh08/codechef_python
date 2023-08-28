""" Eikooc loves bread. She has N loaves of bread, all of which expire after exactly 
M days. She can eat upto K loaves of bread in a day. Can she eat all the loaves of bread before they expire? """

# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    breads= y*z
    if breads >= x:
        print("yes")
    else:
        print("no")
