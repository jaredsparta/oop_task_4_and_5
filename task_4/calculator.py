from math import sin, pi

class Calculator:
    def __init__(self):
        pass

    # Adds two numbers together
    def add(self, num1, num2):
        return num1 + num2

    # Subtracts num1 from num2
    def subtract(self, num1, num2):
        return num1 - num2

    # Multiplies the two numbers
    def multiply(self, num1, num2):
        return num1 * num2 

    # Divides num1 by num2, raises zero division error if num2 = 0
    # And will output the string
    def divide(self, num1, num2):
        try:
            return num1 / num2
        except:
            return "Can't divide by 0!"

    # Checks divisibility
    def divisibleby(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    # Calculates the area of a triangle given base, height
    def triangle_area_bh(self, base, height):
        return 0.5 * base * height

    # Calculates area of a triangle using the other formula
    def triangle_area_trig(self, side1, side2, angle):
        return 0.5 * side1 * side2 * sin(angle*pi/180)

    # Converts inches to cm
    def inch_to_cm(self, inches):
        return inches * 2.54

    # Converts cm to inches
    def cm_to_inch(self, cm):
        return cm / 2.54

cal = Calculator()


