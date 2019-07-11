'''
This is the example we all did as a class. I have provided it for you in case you missed some of the information or need
clarification.
'''

def get_age():
    age = input("How old are you? ")
    age = int(age)
    print("In 50 years, you'll be", str(age+50)+".")
    return age

def get_birth_year(age):

    #Get the current year
    year = input("What year is it? ")
    year = int(year)

    #Find the birth year
    birth_year = year-age

def main():
    #Now we are going to get the user's name.
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name? ")
    last_name = input("What is your last name? ")

    print(first_name, middle_name, last_name)

    #Store the return value of get_age in a variable called age
    age = get_age()

    #Pass the value of age into the get_birth_year function
    get_birth_year(age)

if __name__ == "__main__":
    main()