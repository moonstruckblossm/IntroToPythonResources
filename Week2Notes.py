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