#Let's decide what we want our pyramid to be made of.

#I chose the asterisk

character = "*"

#Now, let's input the height of the pyramid.
height = int(input("Enter the height of the pyramid: "))

#Remember, when you multiply a string by a number...
#It will produce n of that string.

#So, with that being said.

#let's initialize a variable i
i = 1

while i <= height: #while i is less than the height of the pyramid...

    # For each element from 1 to height...
    for x in range(1, height + 1):  # add one so the pyramid will have the correct height (start at 1)

        # Print i number of characters.
        print(character * x)

    i = i+1


