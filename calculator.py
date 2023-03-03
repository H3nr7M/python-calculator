# define the calculator function
def calculator():

    # display the available operations
    print("Please select operation -")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # get the user's choice of operation
    # and convert it to an integer because input() returns a string
    choice = int(input("Enter operation number: "))

    # get the two numbers to perform the operation on
    # and convert it to an integer because input() returns a string
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # perform the selected operation
    # we use the if-elif-else statement to check the user's choice
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2
    else:
        print("Invalid operation")
        return

    # print the result
    # f strings are used to format the string in Python 3.6+ it's really helpful for cleaner code
    print(f"Result: {result}")


# call the calculator function
calculator()
