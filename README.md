import math
radius = float(input("Input the radius of the circle : "))
area = math.pi * radius * radius
print("Area of the circle is :{0}".format(area))



filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

