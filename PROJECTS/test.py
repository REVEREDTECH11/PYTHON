def square(b,h):
    area = b * h
    print(area)
    
def square_details():
    print("Formula is base * height")
    b = int(input("Height"))
    h = int(input("Base"))
    square(b,h)
    

square_details()
