'''
This is the first activity that we did on Jul 22, with comments.
'''


#First, let's initialize our sum and get input from the user.
sum = 0
num = int(input(">>Please enter a number (enter a negative number to quit): "))


#Now we can create our while loop. I
while num >= 0:

    #Here, we add the number we got to the sum we initialized.
    sum += num
    print(sum)

    #Ask for another number, which must be positive.
    num = int(input(">>Please enter a number (enter a negative number to quit): "))

#Print out the final sum when the loop is broken
print(">>The total sum of all the numbers enetered is", sum)

