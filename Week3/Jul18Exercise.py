'''
This file contains the pangram activity done on 7/18/19.
'''



def checkPangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in string:
            return False
    return True

def main():
    print("Welcome!")
    print()
    print("This program checks a string to find if it is a pangram.")

    choice = "Yes"

    while choice == "Yes":
        sentence = input("Enter a string to be checked: ")
        ans = checkPangram(sentence)
        if ans:
            print("This is a pangram.")
        else:
            print("This is not a pangram.")
        choice = input("Play again? Yes/No: ")
    print("Goodbye!")
main()