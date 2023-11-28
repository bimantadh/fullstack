import math

def scientific_calculator():
    print("Scientific Calculator")

    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square root")
        print("6. Trigonometric functions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

        if choice == '1':
            result = num1 + num2
            print("Result: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Result: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Result: ", result)
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print("Result: ", result)
        elif choice == '5':
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            if num < 0:
                print("Error! Square root of a negative number is undefined.")
            else:
                result = math.sqrt(num)
                print("Result: ", result)
        elif choice == '6':
            angle = float(input("Enter the angle in degrees: "))
            angle_radians = math.radians(angle)
            print("Trigonometric functions:")
            print("Sin(", angle, "): ", math.sin(angle_radians))
            print("Cos(", angle, "): ", math.cos(angle_radians))
            print("Tan(", angle, "): ", math.tan(angle_radians))
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    scientific_calculator()