""" You know that 
1 kg of pulp can be used to make
1000 pages and 1 notebook consists of 100 pages.
Suppose a notebook factory receives N kg of pulp, how many notebooks can be made from that? """

for _ in range(int(input())):
    p=int(input())
    print((p * 1000) //100)
