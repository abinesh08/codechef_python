import itertools,random
shuffle=list(itertools.product(range(1,14),['spade','Heart','queen','king']))
random.shuffle
print('the cards are')
for i in range(5):
    print(shuffle[i][1])
