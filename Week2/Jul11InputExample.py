'''
This is the example we all did as a class. I have provided it for you in case you missed some of the information.
'''

def get_age():
    age = input("How old are you? ")
    age = int(age)
    print("In 50 years, you'll be", str(age+50)+".")

def main():
    #Now we are going to get the user's name.
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name? ")
    last_name = input("What is your last name? ")

    print(first_name, middle_name, last_name)

    get_age()

if __name__ == "__main__":
    main()