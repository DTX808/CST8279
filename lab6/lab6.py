# def CelToFahr():
#     far = float(input('Enter temp in Fahrenheit: '))
#     celsius = (far - 32) * (5/9)
#     print(f'{far}°F= {celsius:2f}°C')
#     return celsius
# CelToFahr()

# def my_min(a,b):
#     if a == b:
#         print(f'{a} is equal to {b}')
#         return a
#     else:
#         mini = a if a < b else b
#         print(f'the smaller number is {mini}')
#         return 
# my_min(30,23)
import math
def VolumeOfSphere(radius: float) -> float:
    """
    Calculate the volume of a sphere using the formula:
    V = 4/3 * pi * r**3
    """
    if radius < 0:
        raise ValueError('Radius must be non-negative')
    return (4/3)*(math.pi)*(radius**3)


print(f'the volume is: {VolumeOfSphere(3)}')


