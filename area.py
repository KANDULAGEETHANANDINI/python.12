class Rectangle:
def calc(self):
  l=int(input("enter l "))
  b=int(input("enter b "))
  print("area is ",l*b)
  print("perimeter of rectangle is ",2*(l+b))
  class Triangle:
 def calc(self):
  x=int(input("enter x "))
  y=int(input("enter y "))
  z=int(input("enter z "))
  s=(x+y+z)/2
  print("area of triangle is ",(s*(s-x)*(s-y)*(s-z))**0.5)
  print("perimeter of triangle is ",(x+y+z))
  class Circle:
 def calc(self):
  r=int(input("enter r "))
  print("area of circle is ",3.14*r*r)
  print("perimeter of circle is ",2*3.14*r)
a=int(input("enter no. of sides"))
if(a==2):
  s=Rectangle()
  s.calc()
elif(a==3):
  t=Triangle()
  t.calc()
elif(a==1):
  c=Circle()
  c.calc()
else:
 print("invalid")