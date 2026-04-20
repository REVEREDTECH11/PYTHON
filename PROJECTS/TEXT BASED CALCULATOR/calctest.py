import math
import numpy as np

def trig_mode():
    print("Triginometry Mode")
    x = 45	
    mode = input("Enter trig mode: ")
    if mode == "cos":
        x_rad = math.cos(math.degrees(math.radians((x))))
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
trig_mode()