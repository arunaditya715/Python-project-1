import math

def area_of_circle(radius):
    if radius < 0:
        print("The radius cannot be negative")
    else:
        area=math.pi *radius **2
        return area
    
try:
    radius=eval(input("Enter thr valid radius of circle"))

except ValueError:
    print("Invalid Output Please enter a valid radius")

else:
    area=area_of_circle(radius)
    if isinstance(area,float):
        print(f"The radius of circle is{radius} is {area:.2f}")
    else:
        print(area)