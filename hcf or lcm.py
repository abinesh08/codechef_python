def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x

    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
a=100
b=2
print("Hcf are",compute_hcf(a,b))



def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
a=200
b=110
print(compute_hcf(a,b))


        



 
    