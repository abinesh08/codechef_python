""" Chef is shopping for masks. In the shop, he encounters 2 types of masks:
Disposable Masks — cost 

X but last only 1 day.
Cloth Masks — cost Y but last 10 days.
Chef wants to buy masks to last him 100 days. He will buy the masks which cost him the least. In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks. Which type of mask will Chef choose? """

for _ in range(int(input())):
    x,y=map(int,input().split())
    disposable = x * 100
    cloth= y *10
    if disposable == cloth:
        print("cloth")
    elif disposable < cloth:
        print("disposable")
    else:
        print("cloth")
        
