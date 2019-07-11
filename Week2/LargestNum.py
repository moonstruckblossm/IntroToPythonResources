'''
In this simple program, the user provides three numbers, and, using three if/elif
statements, the largest number is determined.

This program uses input, typecasting, conditionals, and logic operators.
'''

def main():
    '''
    This is the main function. In this function, the user is prompted to give 3 numbers, all of which are
    typecast to integers. Using a series of conditionals, the largest number is determined, and that number
    is printed.
    :return: None
    '''


    #The user is prompted for three different numbers
    x = int(input("Enter num 1: "))
    y = int(input("Enter num 2: "))
    z = int(input("Enter num 3: "))

    #A series of if/elif/else statements to check to see what number is the highest.
    if x > y and x > z:
        largest = x
    elif y > x and y > z:
        largest = y
    elif z > x and z > y:
        largest = z
    else:
        #This else condition will only execute if all numbers are the same. The largest will default to x.
        largest = x

    #The largest number is printed.
    print(str(largest)+" is the largest number!")

main()