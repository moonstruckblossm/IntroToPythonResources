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



#--FUNCTIONS--#

#Functions are sequences that may or may not return values.
#An example of a function that does not return a value is print().

#In order to return a value from a function make sure that you add a "return statement" (return()) at the end.

#Examples of functions that do return something are the lower() and upper() function.
#These functions will return uppercase and lowercase, respectively, versions of any string you give it
#This function does NOT change the actual variable!

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
