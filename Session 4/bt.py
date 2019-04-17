from math import sqrt
a = int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))
delta=(b**2-4*a*c)
print ("delta: ",delta)
x1 = ((-b+sqrt(delta))/2)
x2 = ((-b-sqrt(delta))/2)
x = (-b/(2*a))
if delta >0:
    print("Pt co 2 ng pb")
    print(x1,x2)
elif delta == 0:
    print("pt co ng k:")  
    print(x)  
else:
    print("pt vo ng")