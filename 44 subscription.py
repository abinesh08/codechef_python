""" A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 
6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
X rupees. Determine the minimum total cost that the group of N friends will incur so that everyone in the group is able to use Chef-TV.  """

for _ in range(int(input())):
    x,y=map(int,input().split())
    if (x%6==0):
        print((x//6)*y)
    elif (x // 6 !=0):
        print(((x//6)+1) * y)
    else:
        print(y)
