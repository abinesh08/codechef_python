#formula = -b +B^2 -sqroot(4ac)/2a
#program eqn= -b+b**2 -4*a*c**0.5/2*a 
#prog eqn =-b-b**2 -4*a*c**0.5/2*a 

#quadratic is a complex form so import cmath:complexmath.
import cmath
a=1
b=5
c=6
#first find d discriminant.
d= b**2 - 4*a*c

solution1= (-b-cmath.sqrt(d))/(2*a)
solution2= (-b+cmath.sqrt(d))/(2*a)
print('quatratic eqn is 1 :', (solution1,solution2))