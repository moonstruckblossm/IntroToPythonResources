'''
This file contains notes for the week of 7/8/2019. This week, we will cover variables, typecasting, functions, methods,
input, the Random module/other modules, conditionals, and loops.
'''

#Last week, we learned about variables and what can and cannot be a variable.

#We also learned the criteria for declaring a variable.

'''
We learned that...
-In order to declare a variable, you must set it EQUAL to the value you want it to be.
-Assignment goes from right to left.
-A variable MUST begin with a letter.
-A variable can contain numbers.
-A variable cannot use any special characters (+, =, #, $, @, etc) besides _ (an underscore).
'''

#In Python, multiple same-line assignments can be done.

#For example...
x, y, z = 1, 2, 3

print(x) #This will produce 1
print(y) #This will produce 2
print(z) #This will produce 3



#--TYPECASTING--#

#In Python and other programming languages, typecasting is when you assign a value of one type to another.

#For example, say you have a string...

aString = "127"
bString = "4.0"

#As you can see, this string is a number. This means that, through typecasting, you can make it an integer!

IntVersion = int(aString)
floatVersion = float(bString)

#This can be done to make an integer, float, boolean, etc. into a string,
print(IntVersion) #This will produce the integer 127
print(floatVersion) #This will produce the float 4.0

#Be mindful, however, that you cannot make string values into integers/floats UNLESS they are eligible.
#What this means is that trying to make the string "cat" into an integer WILL not work.



#--FUNCTIONS AND METHODS--#

#Functions are sequences that may or may not return values.
#An example of a function that does not return a value is print().

#In order to return a value from a function make sure that you add a "return statement" (return()) at the end.

#Examples of functions that do return something are the lower() and upper() function.
#Lower() and upper() are METHODS of a string.
#These methods will return uppercase and lowercase, respectively, versions of any string you give it
#These methods do NOT change the actual variable!

x = "hey everyone"
xUpper = x.upper()
print(xUpper) #This will produce "HEY EVERYONE"

#As seen in this example, you can save the result of this function by placing it into a variable.

y = "HEY HEY"
yLower = y.lower()
print(yLower) #This will produce "hey hey"

#You can overwrite the variables x and y by re-declaring them.

y = y.lower()
#Now, y is equal to "hey hey"

#You can use the function dir() to find out all of an object's methods!
print(dir(str)) #This will produce all methods of a string.
#The functions with underscores in them are called with a superclass.

#The word "str" in the dir function call is an ARGUMENT or PARAMETER.
#This means that the function will use what you gave it when it executes.



#--WRITING FUNCTIONS--#

#In order to write a function, we must consider some things...

'''
-The function needs a name. 
-The name cannot start with a number or underscore, but may contain them.
-The function must be defined and called with parentheses.
'''

#Here is how you define a function!
def function1():
    #All of the function code goes in here! The code is indented.
    #This is called "scope"
    print("Henlo everyone!")

#This comment, because of its indentation level, is not inside of the function definition!
#Since we have declared this function, we can call it at any time.
function1()

#You cannot call a function before it is defined! This will produce an error!
#Python reads line-by-line. If a function call comes before a function, the program hasn't seen the declaration yet.



#--FUNCTION PARAMETERS--#

#To pass something to a function, you place it into the parentheses of the function's definition.
#For example...

def someFunc(name):
    print("My name is "+name+"!")
someFunc("Jimin") #This will produce "My name is Jimin!"

#Here's the example we did in class.
def editFunction(word):
    name = "NCT " #This declares the word
    name = name+word #This will ADD the word from the parameter to the word you already have, overwriting it.
    return name #This returns the full word for you to use outside of the function
print(editFunction("127")) #This will produce "NCT 127"



#--MAIN FUNCTION--#


def func1():
    print("I am a function!")

#The main function is where you will write most of the functionality of the program.
#This function is called last in a program and will contain most of your program's functionality.
#In main, you can call all other functions in any order that you want.

#The way that you declare the main function is...

def main():
    print("Hello world!")
    func1() #This will call func1()
if __name__ == "__main__":
    main()

#You can call another function in your main too, as seen above.



#--CONDITIONALS AND CONTROL LOGIC--#

#A conditional, or an if/else/elif statement is something you can use in your program to operate with logic.

#Here's how they work.

'''
IF = This will check if the following statement is true
ELSE = This will be paired with an if statement, and will execute if the if statement was not true
ELIF = This will be paired with an if statement, and will execute if the if statement was not true, and contains a
statement. There can be multiple elifs in a chain of statements.

AND = If one factor AND another are both true, the if statement will execute
OR = If at least one factor OR the other is true, the if statement will execute
NOT = If the opposite of all factors in the statement is true, the if statement will execute.
'''

#Just like in order of operations, operations in parentheses will execute first.

#Here is an example.

a = True
b = False
c = True

if (a and b) or (not c):
    print("I am false!") #This will not execute.

'''
Notice how that code didn't execute?

a is true, and b is false. This will produce false. c is true, and NOT c will produce false. Therefore, the statement
false or false equals false, so the code inside will not execute.
'''

if (a and not b) or (not c):
    print("This one is true!") #This WILL execute!

'''
a is true, and b is false. NOT b is true, so true and true, equals true. If any factor of an OR statement is true, the
whole statement is true. Therefore, the code will execute.
'''