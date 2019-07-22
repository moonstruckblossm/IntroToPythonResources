'''
This is the example we did in class on July 15.
'''


def get_username():
    '''
    This function gets the user's username and finds the length of it. Then, it returns the username for the mainm
    function to user.
    :return: Username, the user's username.
    '''

    #First, let's get the user's username.
    username = input("Enter your username: " )
    #We can print it out
    print(username)

    #Now, let's user the len() function to find the length of the username we just got.
    #We can save it to a variable
    username_length = len(username)

    #Finally, let's make a string describing how long the username is.
    print("Your username is", username_length, "characters long.")

def check_leap_year():
    '''
    This function checks to see if the current year is a leap year. It's a little advanced, but
    :return: None.
    '''
    year = input("Enter the current year: ")

    #Let's make sure that the year is an integer.
    year = int(year)

    #If the year is a multiple of 4...
    if year%4 == 0:
        #Print that the year is a leap year in this case.
        print(year, "is a leap year.")

    #If it is NOT a multiple of 4...
    else:
        #Print that it is not a leap year.
        print(year, "is not a leap year.")

def check_numbers():
    '''
    This function asks the user to provide 3 numbers. These numbers are then compared in order to find the largest
    out of the three using a series of if/elif statements.
    :return: none
    '''

    #Get three numbers from the user.
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    num3 = input("Enter one last number: ")

    #Make sure that those numbers are integers
    a = int(num1)
    b = int(num2)
    c = int(num3)


    #You COULD take in all three numbers at the same time and split them to make inputting faster...

    #Use a series of if statements to compare all of the numbers to each other.
    if a >= b and a >= c:
        #Right here, you can print a. I just put it into the variable "largest" to print later.
        largest = a
    elif b >= a and b >= c:
        largest = b
    #You've checked all other conditions, so you can just use "else". Largest defaults to c.
    else:
        largest = c

    #This prints the largest number.
    print(str(largest)+" is the largest number!")

def main():
    '''
    The main function in this program mostly serves to store values and call the other functions.
    :return: none
    '''

    #First, welcome!
    print("Guh-huh!")

    #Call get_username() and store the username you are given
    get_username()

    #Calls the check_leap_year() function.
    check_leap_year()

    #Calls the check_numbers function.
    check_numbers()

if __name__ == "__main__":
    main()

