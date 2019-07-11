'''
This program takes a number and, using a function called isPrime(), checks to see if that
number is a prime number.

This program uses functions, parameters, returning, booleans, for loops, input, typecasting, and
conditionals.
'''

def isPrime(num):
    '''
    This function checks to see if a number is a prime number or not using a series of ocnditionals and a
    for loop. If the number is prime, then True is returned. If not, False is returned.
    :param num: The number to be checked
    :return: A boolean referring to whether or not the number is prime or not.
    '''

    if -4 < num < 4: #If the number is less than 4 and greater than -4, it is prime...
        return True #...so True is returned
    else: #If it is not less than 4 and greater than -4...
        for i in range(2, 6): #Loop through all numbers in the range 2 to 6 (not including 6!)
            if num%i == 0: #If it divides evenly...
                return False #It is not a prime number
    return True #If no conditions are met, return True by default.

def main():
    '''
    This function is the main function. In this function, the user is prompted to input a number. That
    number is then passed to the isPrime() function as the parameter num. Based on the value returned by
    isPrime(), the program will print whether or not the function is prime.
    :return: None
    '''
    num = int(input("Enter a number: "))
    result = isPrime(num)
    if result:
        print("This number is prime!")
    else:
        print("This number is not prime!")

main()