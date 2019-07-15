'''
This is the example we all did as a class. I have provided it for you in case you missed some of the information or need
clarification.
'''

def get_age():
    '''
    This function uses an input to find out the user's age and, using that given value, calculates how old the user will
    be in 50 years. This function also RETURNS the original value of age to the main function.
    :return: The age that the user inputs.
    '''
    age = input("How old are you?\n") #This function asks how old the user is...
    age = int(age) #Typecasts the age into an integer so it can be added...
    print("In 50 years, you'll be", str(age+50)+".") #Calculates how old the user will be in 50 years...
    return age #Returns the original value of age.

    #Notice how the original value "age" is never actually changed by this function.

def get_birth_year(age):
    '''
    This function takes in an age and uses it to find the year the user was born.
    :param age: The age of the user.
    :return: The user's birth year.
    '''

    #Get the current year...
    year = input("What year is it?\n")

    #Make that input into an integer...
    year = int(year)

    #Ask the user if they've had their birthday yet.
    bday = input("Have you had your birthday yet? Enter yes or no:\n")

    #Check to see what value the user entered...
    if bday.lower() == "yes":
        print("You were born in the year", year-age, ".")
    else:
        #In addition, you could reassign age by re-declaring the variable for age and adding one...
        print("You were born in", year-(age+1), ".")

def main():

    #Now we are going to get the user's name.
    first_name = input("What is your first name?\n")
    middle_name = input("What is your middle name?\n")
    last_name = input("What is your last name?\n")

    #Here, your first, middle, and last name will be printed together...
    print(first_name, middle_name, last_name)

    #Store the return value of get_age in a variable called age...
    age = get_age()

    #Pass the value of age into the get_birth_year function...
    get_birth_year(age)

if __name__ == "__main__":
    main()