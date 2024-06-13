import math

print("===============")
print("Area Calculator")
print("===============")
print()

# Function to list the available shapes and prompt the user to select one.
def list_shapes():
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Circle")
    print("5. Quit")
    print()
    shape = int(input("Which shape: "))
    print()
    return shape

# Get the user's shape choice
shape = list_shapes()

# Function to calculate and print the area of a triangle
def triangle():
    base = int(input("Base: "))
    height = int(input('Height: '))
    print()
    triangle_area = (height * base) / 2
    print(f'The Area is {triangle_area}')
    print()

# Function to calculate and print the area of a rectangle
def rectangle():
    width = int(input("Width: "))
    height = int(input('Height: '))
    print()
    rectangle_area = height * width
    print(f'The Area is {rectangle_area}')
    print()

# Function to calculate and print the area of a square
def square():
    side = int(input("Side: "))
    print()
    square_area = side ** 2
    print(f'The Area is {square_area}')
    print()

# Function to calculate and print the area of a circle
def circle():
    radius = int(input("Radius: "))
    print()
    circle_area = math.pi * radius**2
    print(f'The Area is {circle_area}')
    print()

# Loop until the user chooses to quit (option 5)
while shape != 5:
    if shape == 1:
        # Calculate the area of a triangle
        triangle()
        shape = list_shapes()
    elif shape == 2:
        # Calculate the area of a rectangle
        rectangle()
        shape = list_shapes()
    elif shape == 3:
        # Calculate the area of a square
        square()
        shape = list_shapes()
    elif shape == 4:
        # Calculate the area of a circle
        circle()
        shape = list_shapes()
    else:
        # Handle invalid shape choice
        print("Invalid shape")
        print()
        shape = list_shapes()
