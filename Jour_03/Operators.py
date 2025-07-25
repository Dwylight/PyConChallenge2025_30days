#Exercices

#1
age = 18

#2
height = 58.0

#3
complex_store = (2 + 5j)

#4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height 
print("The area of the triangle is:",area)

#5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:",perimeter)

#6
lenght = float(input("Enter lenght:"))
width = float(input("Enter width:"))
perimeter = 2 * (lenght + width) 
print("The perimeter of the rectangle is:",perimeter)

#7
from math import pi, sqrt 
radius = float(input("Enter the radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print("The area of circle is :", area, "and he circumference is: ", circumference)

#8
y = 2 * x - 2
x = (y + 2)/2
x_1 = 5
x_2 = 8
y_0 = 2 * 0 - 2
y_1 = 2 * x_1 - 2
y_2 = 2 * x_2 - 2
slope_1 = (y_2 - y_1) / (x_2 - x_1) 
print("The slope is: ", slope_1)
x_intercept = (0 + 2)/2
y_intercept = y_0
print ("x-intercept = (",x_intercept,";","0)")
print("y-intercept = (0;",y_intercept,")")

#9
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
slope_2 = (y_2 - y_1) / (x_2 - x_1) 
print("The slope is: ", slope_2)
euclidian_distance = sqrt((x_2**2 - x_1**2) + (y_2**2 - y_1**2))
print("The euclidian distance is :", euclidian_distance)

#10
print("slope_2 > slope_1:",slope_2 > slope_1 )

#11
x = float(input("Enter x:"))
y = x**2 + 6*x + 9
print(y)
delta = 6**2 - (4 * 9)
x_0 = -6 / 2
print ("y is going to be 0 at :", x_0)

#12
print("The lenght of python is:",len("python"))
print("The lenght of dragon is:",len("dragon"))
print("python is dragon:", "python" is "dragon" )

#13
print("on in python and dragon:", "on" in ("python" and "dragon"))

#14
print("jargon in  I hope this course is not full of jargon :", "jargon" in " I hope this course is not full of jargon")

#15
print("on" not in ("dragon" and "python" ))

#16
print(len("python"))
print(float(len("python")))
print(str(float(len("python"))))


#17
number = int(input("Enter the number: "))
print(number,"is an even number:", (number % 2) == 0)

#18
a = 7 // 3
b = int(2.7)
print(a == b)

#19
print(type("10") is type(10))

#20
print((int(9.8)) == 10)

#21
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
earning = hours * rate
print("Your weekly earning is: ",earning)

#22
years = int(input("Enter number of years you have lived:"))
second = years * 365 * 24 * 3600
print("You have lived for ",second, "seconds")

#23
print("1 1 1 1 1" )
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125" )

 
 
