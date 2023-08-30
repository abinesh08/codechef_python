""" Bob has an account in the Bobby Bank. His current account balance is W rupees.Each month, the office in which Bob works deposits a fixed amount of X rupees to his account.
Y rupees is deducted from Bob's account each month as bank charges.
Find his final account balance after Z months. Note that the account balance can be negative as well. """

# cook your dish here
for _ in range(int(input())):
    W,X,Y,Z=map(int,input().split())
    balance= X - Y 
    print(W + balance * Z)
