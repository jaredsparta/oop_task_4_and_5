from math import sin, pi

class Calculator:
    def __init__(self):
        pass

    
    def add(self, num1, num2):
        return num1 + num2


    def subtract(self, num1, num2):
        return num1 - num2

    
    def multiply(self, num1, num2):
        return num1 * num2 


    def divide(self, num1, num2):
        try:
            return num1 / num2
        except:
            return "Can't divide by 0!"


    def divisibleby(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def triangle_area_bh(self, base, height):
        return 0.5 * base * height

    def triangle_area_trig(self, side1, side2, angle):
        return 0.5 * side1 * side2 * sin(angle*pi/180)


cal = Calculator()
print(cal.triangle_area_trig(5,6,90))