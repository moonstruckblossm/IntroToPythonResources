#Let's get a height.
height = int(input("Enter a number: "))

#Let's establish our counter.
counter = 1

#Let's put it in an infinite loop. Just because ;D
while True:
    #While counter is less than height...
    while counter <= height:

        #Print counter num of asterisks
        print("*" * counter)

        #increment counter
        counter = counter+1

    #Then we do it back the other way.
    while counter > 0:
        print("*" * counter)

        #Make sure to increment the counter back down! If you don't, it will be infinite.
        counter = counter-1