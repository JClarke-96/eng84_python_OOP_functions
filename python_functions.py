# How to create a function
# Syntax for a function: def function_name():

# Creating a function
def greetings(name):
    print("Welcome to the calculator, " + name)

# Function to add two numbers when called
def add(num1, num2):
    return (num1 + num2)


# Function to subtract one number from the other
def subtract(num1, num2):
    return (num1 - num2)


# Function to multiply two numbers
def multiply(num1, num2):
    return (num1 * num2)


# Function to divide one number by another
def divide(num1, num2):
    return (num1 / num2)

def calculator():
    calculator_use = input("What would you like to use this caluclator for? (ADD/ SUBTRACT / MULTIPLY / DIVIDE)   ")
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    if calculator_use == "ADD":
        print(add(num1, num2))
    elif calculator_use == "SUBTRACT":
        print(subtract(num1, num2))
    elif calculator_use == "MULTIPLY":
        print(multiply(num1, num2))
    elif calculator_use == "DIVIDE":
        print(divide(num1, num2))
    else:
        print("Incorrect input, please try again")
        calculator()


name = input("What is your name?    ")
greetings(name)
calculator()