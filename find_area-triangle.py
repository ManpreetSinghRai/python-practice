# how to find area of triangle
a = 5
b = 6
c = 7
# calculate the semi-perimeter
s = (a+b+c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of triangle is %0.2f" % area)
