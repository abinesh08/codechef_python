def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    
    while(True):
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return(lcm)


a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
result_lcm = compute_lcm(a, b)
compute_lcm('lcm is:',result_lcm)