import time
import math
#import tkinter as tk

#section for basic math
def addition():
    print("Addition mode")
    variable_a = int(input("Enter the first value: "))
    variable_b = int(input("Enter the second value: "))
    result = float(variable_a + variable_b)
    print(f"{variable_a} plus {variable_b} is {result}")

def subtraction():
    print("Subtraction mode")
    variable_a = int(input("Enter the first value: "))
    variable_b = int(input("Enter the second value: "))
    result = float(variable_a - variable_b)
    print(f"{variable_a} minus {variable_b} is {result}")

def multiplication():
    print("Multiplication mode")
    variable_a = int(input("Enter the first value: "))
    variable_b = int(input("Enter the second value: "))
    result = float(variable_a * variable_b)
    print(f"{variable_a} times {variable_b} is {result}")
    
def division():
    print("Division mode")
    variable_a = int(input("Enter the first value: "))
    variable_b = int(input("Enter the second value: "))
    result = float(variable_a / variable_b)
    print(f"{variable_a} divided {variable_b} is {result}")
    
def squareroot():
    print("Squareroot mode")
    variable = int(input("Enter Value: "))
    square_root = math.sqrt(variable)
    print(square_root)
#section for basic math


#area of a triangle start
def area_of_triangle():
    area = ((1/2) * b * h)
    print(f"The area is {area}")

def aot_details():
    print("The formula to find the area of a triangle is (1/2)b*h.")
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area_of_triangle(b,h)
#area of a triangle end
    
#area of a square start
def area_of_square(b,h):
    area = b * h
    print(f"The area of the square {area}")
    
def square_details():
    print("Formula is base * height")
    b = int(input("Enter height "))
    h = int(input("Height base "))
    area_of_square(b,h)
#area of a square end
    
def trig_mode():
    x = int(input("Enter number "))
    mode = input("Enter trig mode ")
    if mode == "cos":
        x_rad = math.radians(x)
        cosValue = math.cos(x_rad)
        cosConvert = math.degrees(cosValue)
        print(f"{round(cosValue,2)} radians")
        print(f"{round(cosConvert,2)} degrees")
    elif mode == "acos":
        x_rad = math.radians(x)
        acosValue = math.acos(x_rad)
        acosConvert = math.degrees(acosValue)
        print(f"{round(acosValue,2)} radians")
        print(f"{round(acosConvert,2)} degrees")
    elif mode == "sin":
        x_rad = math.radians(x)
        sinValue = math.sin(x_rad)
        sinConvert = math.degrees(sinValue)
        print(f"{round(sinValue, 2)} radians")
        print(f"{round(sinConvert, 2)} degrees")
        print(f"{sinValue:.2f}")
    elif mode == "asin":
        x_rad = math.radians(x)
        asinValue = math.asin(x_rad)
        asinConvert = math.degrees(asinValue)
        print(f"{round(asinValue, 2)} radians")
        print(f"{round(asinConvert, 2)} degrees")
    elif mode =="tan":
        x_rad = math.radians(x)
        tanValue = math.tan(x_rad)
        tanConvert = math.degrees(tanValue)
        print(f"{round(tanValue, 2)} radians")
        print(f"{round(tanConvert, 2)} degrees")
    elif mode =="atan":
        x_rad = math.radians(x)
        atanValue = math.atan(x_rad)
        atanConvert = math.degrees(atanValue)
        print(f"{round(atanValue, 2)} radians")
        print(f"{round(atanConvert, 2)} degrees")
    else:
        print("Invalid mode")
        trig_mode()

def derivatives():
    print("Not finieshed")

def floor():
    print("Not finieshed")

def ceiling():
    print("Not finieshed")

def power():
    print("Not finieshed")

def log():
    print("Not finieshed")
    
def countdown(seconds):
    print("WELCOME TO THE CALCULATOR!!")
    print("BY LAMAR-SWE")
    while seconds:
        time.sleep(1)
        seconds -= 1
countdown(2)

print("\nWe offer")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Area of Triangle")
print("7. Area of Square")
print("8. Trigonometric Functions")
print("9. Derivatives")
print("10. Floor")
print("11. Ceiling")
print("12. Power")
print("13. Logarithm")
mode = int(input("Please select a mode: "))

if mode == 1:
    addition()
elif mode == 2:
    subtraction()
elif mode == 3:
    multiplication()
elif mode == 4:
    division()
elif mode == 5:
    squareroot()
elif mode == 6:
    aot_details()
elif mode == 7:
    square_details()
elif mode == 8:
    trig_mode()
else:
    print("Goodbye")
