'''
This file contains the pangram activity done on 7/18/19.

A pangram is a sentence that contains all letters of the alphabet.
'''


#This is the function that will check if a sentence is a pangram.
def checkPangram(string):

    #First, we can save the whole alphabet to a variable.
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #For each letter in the alphabet...
    for i in alphabet:

        #If a letter is NOT in the string you provide...
        if i not in string:
            #It will return False
            return False

    #If not, then it will return True
    return True

#This is where the user will give the program the string, and where the function will be called.
def main():
    print("Welcome!")
    print()
    print("This program checks a string to find if it is a pangram.")

    #Here is the default string.
    choice = "Yes"

    #While the choice is "Yes" for whether or not you want to play again...
    while choice == "Yes":

        #Get a string from the user.
        sentence = input("Enter a string to be checked: ")

        #Check to see if it is a pangram.
        ans = checkPangram(sentence)

        #If ans = True, it is a pangram
        if ans:
            print("This is a pangram.")

        #If ans = False, it is not a pangram.
        else:
            print("This is not a pangram.")

        #The user is asked whetehr or not they want to play again.
        choice = input("Play again? Yes/No: ")

    #If choice = no, this message will print.
    print("Goodbye!")
main()