'''
This program uses a conditional to determine whether or not a number it is given is even
or odd. This program, unlike the other EvenOddTest.py program, uses a loop so that the
user may input multiple numbers.

This program uses conditionals, parameters, functions, while loops, returning,
typecasting, and operators.
'''


def isEvenOdd(num):
    '''
    In this function, the parameter num is divided by 2 to see if the remainder is 0 or not. If the
    remainder is 0, the number is even, and the value returned is "even". If it is not 0, the number is
    odd, and the value returned is "odd".
    :param num: The number to be checked.
    :return: The strings "even" or "odd", depending on which the number is.
    '''
    if num%2 == 0:
        return "even"
    else:
        return "odd"

def main():
    '''
    In this main function, a while loop is created in order to check multiple numbers. Each number is
    passed into the isEvenOdd() function (unless it is "quit", which stops the loop), and the result is
    printed at the end.
    :return: None
    '''

    #Loops forever until quit.
    while True:

        #User is prompted to enter a number.
        num = input("Enter a number: ")

        #If number is "quit", the loop breaks.
        if num == "quit":
            print("Goodbye!")
            break

        #If not, the function continues and the loop starts again after the
        else:

            #Number is typecast to an int...
            num = int(num)
            #The return value is saved to a value called result...
            result = isEvenOdd(num)
            #Result is printed.
            print("This number is "+result)

main()