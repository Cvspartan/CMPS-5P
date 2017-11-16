import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/float(3))*math.pi*radius**3
surface_area = 4*math.pi*radius*radius

print("The volume is: "+str(volume))
print("The surface area is "+str(surface_area))
                                             
