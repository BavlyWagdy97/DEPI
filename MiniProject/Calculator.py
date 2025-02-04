def Add(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Mult(num1, num2):
    return num1 * num2

def Div(num1, num2):
    if num2 == 0:
        return "Math Error"  
    return num1 / num2

while True:
    print("\nPlease Enter Your Operation's Number:\n 1 - Add\n 2 - Sub\n 3 - Mult\n 4 - Div")

    try:
        Operation = int(input("Enter choice (1/2/3/4): "))
        num1 = float(input("Please Enter First Number: "))
        num2 = float(input("Please Enter Second Number: "))

        if Operation == 1:
            print("Result:", Add(num1, num2))  
        elif Operation == 2:
            print("Result:", Sub(num1, num2))
        elif Operation == 3:
            print("Result:", Mult(num1, num2))
        elif Operation == 4:
            print("Result:", Div(num1, num2))
        else:
            print("Invalid Operation! Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    Status = input("If You Want to Continue, Enter 1; Else Enter 0: ")
    if Status == '0':
        print("Exiting Calculator. Goodbye!")
        break
