import math

def calculate_surface_perimeter():
    print("Choose a geometric shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        surface = side ** 2
        perimeter = 4 * side
        print(f"Surface area: {surface} | Perimeter: {perimeter}")
    
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        surface = length * width
        perimeter = 2 * (length + width)
        print(f"Surface area: {surface} | Perimeter: {perimeter}")
    
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        surface = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius
        print(f"Surface area: {surface} | Perimeter: {perimeter}")
    else:
        print("Invalid choice. Please try again.")

calculate_surface_perimeter()
