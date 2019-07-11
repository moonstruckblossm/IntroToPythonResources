'''
This program uses an if/else block in order to determine whether or not a number it is
given is even or odd.

This program uses conditionals, parameters, functions, input, typecasting, operators,
and returning.
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
    In this main function, a number is passed into the isEvenOdd() function, and the result is printed at the end.
    :return: None
    '''

    # User is prompted to enter a number.
    num = input("Enter a number: ")
    # Number is typecast to an int...
    num = int(num)
    # The return value is saved to a value called result...
    result = isEvenOdd(num)
    # Result is printed.
    print("This number is "+result)

main()