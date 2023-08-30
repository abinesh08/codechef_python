""" Chef's playlist contains 3 songs named 
A,B, and 
C, each of duration exactly 
X minutes. Chef generally plays these 3 songs in loop, i.e, 
A→B→C→A→B→C→A→…
Chef went on a train journey of 
N minutes and played his playlist on loop for the whole journey. How many times did he listen to the song C completely?Input Format
The first line of input will contain a single integer 
T, denoting the number of test cases. The description of the test cases follows.
Each test case consists of a single line of input, containing two space-separated integers N,X. """

for _ in range(int(input())):
    a,b=map(int,input().split())
    c= 3*b 
    print(a // c)
            
