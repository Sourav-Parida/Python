#Main Program importing modules
#This program allows the user to choose various
# geometrical calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle
choice = 0
ch = "y"
# The display-menu function displays a menu.
#def displaymenu():
while (ch == "y"):
    print("MENU")
    print("1. Area of a circle")
    print("2. Circumference of a circle")
    print("3. Area of a rectangle")
    print("4. Perimeter of a rectangle")
    print("5. Quit")
    choice = int(input ("Enter your choice :"))
    if (choice == 1):
        radius = int(input("Enter the circle's radius: "))
        print("The area is",circle.area(radius))
    elif (choice == 2):
        radius = int(input("Enter the circle's radius: "))
        print("The circumference is",circle.circumference(radius))
    elif (choice == 3):
        width = int(input("Enter the rectangle's width: "))
        length = int(input("Enter the rectangle's length: "))
        print('The area is',rectangle.area(width, length))
    elif (choice == 4):
        width = int(input("Enter the rectangle's width: "))
        length = int(input("Enter the rectangle's length: "))
        print('The perimeter is ',rectangle.perimeter(width, length))
    elif (choice == 5):
        print('Exiting the program ...')
    else:
        print('Error: invalid selection.')


    













