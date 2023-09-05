def add(x,y):
    return (x+y)
def sub(x,y):
     return(x-y)
def multiplication(x,y):
     return(x*y)
def division(x,y):
     return(x/y)

while(True):
     choice=input("give a operations:")
     if choice in ('add','sub','multiplication','division'):
          num1=float(input("Enter the first number:"))
          num2=float(input("Enter the second number:"))

          if choice=='add':
               b=(add(num1,num2))
               print(b)
          elif choice=='sub':
                b=(sub(num1,num2))
                print(b)
          elif choice=='multiplication':
               b=(multiplication(num1,num2))
               print(b)
          elif choice=='division':
               b=(division(num1,num2))
               print(b)
          next_calc= input("next calc yes or no:")
          if next_calc =="no":
               break
     else:
          print("invalid code")
          

          
