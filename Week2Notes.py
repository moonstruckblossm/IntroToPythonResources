'''
This file contains notes for the week of 7/8/2019. This week, we will cover variables, typecasting, functions, methods,
input, the Random module/other modules, conditionals, and loops.
'''

#Last week, we learned about variables and what can and cannot be a variable.

#We also learned the criteria for declaring a variable.

'''
We learned that...
-A variable MUST begin with a letter.
-A variable can contain numbers.
-A variable cannot use any special characters (+, =, #, $, @, etc) besides _ (an underscore)
'''


#--TYPECASTING--#

#In Python and other programming languages, typecasting is when you assign a value of one type to another.

#For example, say you have a string...

aString = "127"

#As you can see, this string is a number. This means that, through typecasting, you can make it an integer!

IntVersion = int(aString)
print(IntVersion) #This will produce the integer 127