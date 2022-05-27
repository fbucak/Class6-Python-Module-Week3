# i. Write a function sphere_volume that calculates and returns the volume of a sphere when given radius r as a parameter.
# ii. Then write a main program that calls sphere_volume to print the volume of a sphere with a radius of 3.
# iii. Write a function sphere that calls two other functions that calculate the area of a circle sphere_area and volume of a sphere sphere_volume for a given radius r as a parameter. Functions sphere_area and sphere_volume are nested inside the function sphere. Function sphere returns both the area and the volume of the sphere. (Reproduce sphere_volume function inside function sphere.) Make sure to print the results.
# Formula to calculate the area of a circle: 𝑨 = 𝝅𝒓𝟐
# Formula to calculate the volume of a circle: 𝑽 = 𝟒/𝟑 𝝅𝒓𝟑
import math
def sphere_volume(r):
    return round(4/3*math.pi*r**3)

def sphere_area(r):
    return round(4*math.pi*r**2)

def sphere(r):
    return "volume of sphere:{} and area of sphere{} ".format(sphere_volume(r),sphere_area(r))
print(sphere(5))
