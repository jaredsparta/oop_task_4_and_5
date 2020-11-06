from math import sin, pi

class Calculator:
    def __init__(self):
        self.body()


    def body(self):
        while True:
            print("-"*30)
            print("""\nPick an option (e.g. input '1' for Addition)
                        1. Add
                        2. Subtract
                        3. Multiply
                        4. Divide
                        5. Check divisibility
                        6. Find the area of a triangle
                        7. Convert centimetres and inches
                        8. EXIT""")
            try:
                choice = int(input("--->  "))
            except:
                continue


            if choice in [1,2,3,4]:
                self.basic(choice)
            
            if choice in [5]:
                try:
                    print("\nChecks if num1 is divisble by num2")
                    num1 = int(input("Please input num1: "))
                    num2 = int(input("Please input num2: "))
                    print(self.divisibleby(num1, num2))
                except:
                    print("\nERROR")

            if choice in [6]:
                print("""\n
                        1. Give base and height
                        2. Give two sides and an angle""")

                choice_2 = int(input("--->  "))                
                self.findarea(choice_2)

            if choice in [7]:
                print("""\n
                        1. Inches to CM
                        2. CM to Inches""")
                choice_2 = int(input("--->  "))
                self.conversion(choice_2)

            if choice in [8]:
                break


    def conversion(self, choice):
        if choice == 1:
            inches = float(input("\nInput a value: "))
            return print(self.inch_to_cm(inches))

        if choice == 2:
            cm = float(input("\nInput a value: "))
            return print(self.cm_to_inch(cm))


    def basic(self, choice):
        if choice == 1:
            try:
                print("\n Computes num1 + num2")
                num1 = float(input("First number to add: "))
                num2 = float(input("Second number to add: "))
                return print(self.add(num1, num2))
            except:
                print("Not a valid option")
                self.basic(1)

        if choice == 2:
            try:
                print("\nWill compute num1 - num2")
                num1 = float(input("Type num1: "))
                num2 = float(input("Type num2: "))
                return print(self.subtract(num1, num2))
            except:
                print("Not a valid option")
                self.basic(2)

        if choice == 3:
            try:
                print("\nWill compute num1 * num2")
                num1 = float(input("Type num1: "))
                num2 = float(input("Type num2: "))
                return print(self.multiply(num1, num2))
            except:
                print("Not a valid option")
                self.basic(3)

        if choice == 4:
            try:
                print("\nWill compute num1 / num2")
                num1 = float(input("Type num1: "))
                num2 = float(input("Type num2: "))
                return print(self.divide(num1, num2))
            except:
                print("Not a valid option")
                self.basic(1)


    def findarea(self, choice):
        if choice == 1:
            try:
                base = float(input("\nInput BASE: "))
                height = float(input("Input HEIGHT: "))
                return print(self.triangle_area_bh(base, height))
            except:
                print("\nOnly valid numbers please")
                self.findarea(1)

        elif choice == 2:
            try:
                side1 = float(input("\nInput first side: "))
                side2 = float(input("Input second side: "))
                angle = float(input("Input angle between the two sides: "))
                return print(self.triangle_area_trig(side1, side2, angle))
            except:
                print("znOnly valid numbers please")
                self.findarea(2)
        else:
            print("\nNo such option")            


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


Calculator()


