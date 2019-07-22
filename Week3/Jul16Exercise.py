
def addNums(num1, num2):
    return num1+num2

def subtractNums(num1, num2):
    return num1-num2

def multiplyNums(num1, num2):
    return num1*num2

def divideNums(num1, num2):
    return num1/num2


def main():

    #Let's first show the user what they can make the program do.
    print("Please select operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")

    #Let's just make a default value of operation for now so it can be changed during the loop.
    operation = "yes"


    #This runs while the operation choice is not 0...
    while operation != "0":

        #The user inputs a number to tell the program which operation they want to use...
        operation = input("Select operation from 1, 2, 3, or 4, or enter 0 to exit: ")


        #If the user's choice is NOT 0...
        if operation != "0":
            #Get the numbers from the user
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))

        #Check to see what operation the user wants to use.
        if operation == "1":
            ans = addNums(num1, num2)
            print(num1, "+", num2, "=", ans)
        elif operation == "2":
            ans = subtractNums(num1, num2)
            print(num1, "-", num2, "=", ans)
        elif operation == "3":
            ans = multiplyNums(num1, num2)
            print(num1, "x", num2, "=", ans)
        elif operation == "4":
            ans = divideNums(num1, num2)
            print(num1, "/", num2, "=", ans)


        #And the loop continues, breaking at the top if the operation choice is 0.

    #This is the message that prints when the loop breaks.
    print("Goodbye!")


if __name__ == "__main__":
    main()