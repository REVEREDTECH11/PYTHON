import time
import math
#import tkinter as tk (will be added later)
#add section for exiting program

def exit():
    prompt = input("Would you like to continue: ")
    promptl = prompt.lower()
    if  promptl == "yes":
        mainMenu()
    else:
        print("Goodbye")
        
def addition():
    print("Addition mode")
    num = int(input("How many problems do you want to answer: "))
    print()
    count = 1
    while (count <= num):
        variable_a = float(input("Enter the first value: "))
        variable_b = float(input("Enter the second value: "))
        #variable_a = 1
        #variable_b = 1
        result = float(variable_a + variable_b)
        print(f"{count}. {variable_a} plus {variable_b} is {result:.3}")
        print()
        count = count + 1
    exit()

#Finished
def subtraction():
    print("Subtraction Mode")
    num = int(input("How many problems do you want to answer: "))
    print()
    count = 1
    while (count <= num):
        variable_a = float(input("Enter the first value: "))
        variable_b = float(input("Enter the second value: "))
        #variable_a = 1
        #variable_b = 1
        result = float(variable_a + variable_b)
        print(f"{count}. {variable_a} plus {variable_b} is {result:.3}")
        print()
        count = count + 1
    exit()


#Finished
def multiplication():
    print("Subtraction Mode")
    num = int(input("How many problems do you want to answer: "))
    print()
    count = 1
    while (count <= num):
        variable_a = float(input("Enter the first value: "))
        variable_b = float(input("Enter the second value: "))
        #variable_a = 1
        #variable_b = 1
        result = float(variable_a + variable_b)
        print(f"{count}. {variable_a} plus {variable_b} is {result:.3}")
        print()
        count = count + 1
    exit()

 
#Finished
def division():
    print("Division mode")
    num = int(input("How many problems do you want to answer: "))
    print()
    count = 1
    while (count <= num):
        variable_a = float(input("Enter the first value: "))
        variable_b = float(input("Enter the second value: "))
        #variable_a = 1
        #variable_b = 1
        result = float(variable_a + variable_b)
        print(f"{count}. {variable_a} plus {variable_b} is {result:.3}")
        print()
        count = count + 1
    exit()

    
def squareroot():
    count = 1
    print("Squareroot mode")
    num = int(input("How many roots are you taking: "))
    while count <= num:
        variable = int(input("Enter Value: "))
        square_root = math.sqrt(variable)
        print(f"{count}. The root of {variable} is {square_root:.3f}")
        print()
        count = count + 1
    exit()
#section for basic math


#area of a triangle start
def area_of_triangle(b,h):
    area = ((1/2) * b * h)
    print(f"The area is {area:.3}")
    exit()
    
def aot_details():
    print("The formula to find the area of a triangle is (1/2) * base * height.")
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area_of_triangle(b,h)
    exit()
#area of a triangle end
    
#area of a square start
def area_of_square(b,h):
    area = b * h
    print(f"The area of the square is {area:.3}")
    exit()
    
def square_details():
    print("The formula to find the area of a square is base * height.")
    b = float(input("Enter height "))
    h = float(input("Height base "))
    area_of_square(b,h)
#area of a square end
    
def trig_mode():
    print("Triginometry Mode")
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

def floor():
    print("Floor Mode")
    numVal = float(input("Enter Value"))
    floorVal = math.floor(numVal)
    print(floorVal)
    
def ceiling():
    print("Ceiling Mode")
    numVal = float(input("Enter Value"))
    ceilingVal = math.ceil(numVal)
    print(ceilingVal)
    
def power():
    powerInput = float(input("Enter number to raise by: "))
    numInput = float(input("Enter number being raised: "))
    result = math.pow(numInput, powerInput)
    print(result)

#Log calculation
def log_calc(x,base):
    results = math.log(x, base)
    print(f"{results:.3f}")
#Log input and push to calculate
def log():
    x = float(input("Enter value to take log of: "))
    base = float(input("Enter base value: "))
    log_calc(x,base)


#countdown for main menu

def mainMenu():
    
    print("\nWe offer")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Area of Triangle")
    print("7. Area of Square")
    print("8. Trigonometric Functions")
    print("9. Floor")
    print("10. Ceiling")
    print("11. Power")
    print("12. Logarithm")
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
    elif mode == 9:
        floor()
    elif mode == 10:
        ceiling()
    elif mode == 11:
        power()
    elif mode == 12:
        log()
    else:
        print("Goodbye")
        #exit()

#countdown for main menu
def countdown(seconds):
    print("WELCOME TO THE CALCULATOR!!!!")
    print("BY LAMAR-SWE")
    while seconds:
        #Timer for menu appearance
        time.sleep(3)
        seconds -= 1
        mainMenu()
#number of loops        
countdown(1)