a = float(input("Enter first side:"))
b = float(input("Enter second side:"))
c = float(input("Enter third side:"))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-b))**0.5
print('area of the triangle %0.2f' % area)
