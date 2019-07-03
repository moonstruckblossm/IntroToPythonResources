'''
These are notes for what was done in class today. If anyone is confused, or has any feedback about these notes, feel
free to send me a message on Slack!
'''



#--PRINTING AND COMMENTS--#
print("This is how you print a line!")
print("Here's how you do...\nTwo lines!") #This will place each side of the \n on different lines.


#This is a single-line comment!
#print("Hello world!")
# ^^ The above print function will not run. It is commented out.

'''
This is a block comment. 
'''




#--TYPES--#

#This is a string!
hiThere = "Hello!"

#This is a boolean! Booleans are always capitalized in Python.
henlo = True
notHenlo = False

#This is an integer!
num = 127

#This is a float!
almost127 = 126.99

#You can NOT add a string and integer/float together, but you can make the integer into a string in order to add them.

print(int("500")) #This will produce 500.

#...And vice versa

print(str(500)) #This will produce "500".

#Making a float an integer will round it DOWN.
print(int(5.7)) #This will produce 5.



#--OPERATORS--#

#Operators include +, -, /, *, **, //, %

'''
+ is addition
- is subtraction
/ is division (will ALWAYS give you a float)
* is multiplication
** is an exponent
// is floor division (will give you an integer )
% is mod (returns the remainder of the operation)
'''
print(0+1) #This will produce 1.
print(8-6) #This will produce 2.
print(49/7) #This will produce 7.0 (note that this is a float).
print(5*3) #This will produce 15.
print(4**2) #This will produce 16.
print(20//5) #This will produce 4 (note that this is an integer).
print(22%5) #This will produce 2.


#We can't really subtract strings, but we can add (concatenate) them.
print("hen"+"lo") #This will produce "henlo".


#We can use indexing to get one letter from a string.

#For example, this is how we can get the letter D out of the word 'Dog':
print("Dog"[0]) #This will produce "D".
#This will find the 0th item in the word. IN ALL LISTS IN PYTHON, THE FIRST ELEMENT IS THE 0TH ELEMENT!


#We can find the size of a list by using the len() method and passing the element into the function.
print(len("Dog")) #This will produce 3; "Dog" has 3 letters.



#--COMPARISON OPERATORS--#

#These operators can be used to compare a variable to another one.

'''
== checks to see if two things are equal
> checks to see if one thing is greater than another
< checks to see if one thing is less than another
>= checks to see if one thing is greater than or equal to another
<= checks to see if one thing is less than or equal to another
!= checks to see if two things are NOT equal

These will all produce booleans, which you can then use.
'''
print(5 == 5) #This will produce True
print("cat" == "dog") #This will produce False

print(5>6) #This will produce False
print("cat" < "dog") #This will produce True.
    #Why does this happen? Each letter has numerical value. This value determines the worth of a string.
    #Capital letters have a lower ASCII value than lowercase letters!
    #In comparing strings, each letter has a value. Strings with more letters have higher values.
    #You can check each letter's value in the ASCII Table.

print(5<2) #This will produce False
print(10<127) #This will produce True

print(90 <= 90) #This will produce True
print(75 >= 100) #This will produce False

print(0 != 0) #This will produce False
print("yes" != "no") #This will produce True



#--VARIABLES--#

#These notes have already used some variables.
#To create a variable, you can use only ONE equals sign.
x = "Cat"
#Now, the string "cat" is stored in x.

#If you set x equal to itself, it's not really setting it equal to itself.
x = x
#This line of code is setting x equal to the VALUE stored in x.


#You can use variables for comparison, too.
one = 1
two = 2

print(one > two) #This will produce False


#Trying to use a variable that has not yet been made will give you an error.
#Python reads line by line, so make sure you have established your variable above the line you use it on!
#Variable names CANNOT start with a number, but they can contain numbers.
#You may use underscores in your variable name, but the underscore CANNOT be in the beginning of the variable.
#Basically, all variable names MUST START WITH A LETTER.
#In order to make your variable names more legible, you can use camelcase, in which each new word in your variable is



#--FUNCTIONS--#

#A function is <INSERT MORE CONCISE DEFINITION HERE>

#This is how you establish a function!
def function1():
    print("Hi there!")
    #All function code goes in here!
function1()
# ^ This is how you call a function that you have already established.

#Call your main function that you create main().
#Remember to call your functions if you want them to execute!


#You can pass a value into a function for it to use. These values are called parameters.
def function2(someInt):
    print(someInt)
function2()

#Given the parameter someInt, the function can use the value stored in someInt.

#NEEDS MORE CONCRETE EXAMPLE- WAIT FOR CLASS EXAMPLE