#This will find the mean of the list of integers that you pass in.
def mean(gradeList):

    #Initialize the variable sum first
    sum = 0

    #For each number in the list, add it to the sum.
    for i in gradeList:
        sum = sum+i

    #Get the length of the list...
    listLen = len(gradeList)

    #Divide the sum by the length to get the mean.
    mean = sum/listLen

    mean = mean//1

    #Finally, print the mean.
    print("The mean of this set of data is", mean)


#This will find the median of the list of integers that you pass in.
def median(gradeList):

    #First, let's get the length of the list.
    length = len(gradeList)

    #Then, we can sort the list.
    gradeList.sort()

    #If the list contains an even number of items, we have to do something extra...
    if length%2 == 0:
        #First, we can get our first middle number
        leftpos = length//2 - 1

        #Then, we'll find the other middle number.
        rightpos = length//2

        #Now, let's use the numbers to access the values at each of those positions
        leftNum = gradeList[leftpos]

        rightNum = gradeList[rightpos]

        #Finally, get the median by adding both nums and dividing them by 2.
        med = (leftNum + rightNum)/2

        #Now print your median!
        print("The median of this set of data is", med)


    #If not, the middle position is just the length floor-divided by 2.
    else:

        #Find the middle position, where the median will be.
        middlePos = length//2

        #Finally, get the median by accessing the value at middlePos
        med = gradeList[middlePos]

        #Now you can print the median!
        print("The median of this set of data is", med)

#This function will find the range of the list of integers you pass in
def Range(gradeList):

    #First, sort your list.
    gradeList.sort()

    #Find the index of the righttmost number.
    largestValIndex = len(gradeList)-1

    #Now, you can get the range using index 0 and the index you just found.
    ran = gradeList[largestValIndex] - gradeList[0]

    #Now you can print your range!
    print("The range of this set of data is", ran)

#This function will find the mode of the list of integers you pass in.
def Mode(gradeList):

    #First, let's sort the list. It will make things easier for us.
    gradeList.sort()

    #Let's say the mode is the first element, for now.
    mode = gradeList[0]

    #Now we can make our for loop, but we need some variables first.

    #This will count how many times the mode has appeared. There is one, because we already saw one.
    modeCount = 1

    #Now we can establish which number is going to challenge the mode
    modeChallenge = -1

    #Let's make a counter that will check to see how many times the challenger appears.
    modeChallengeCount = 0


    #Now, we can make our for loop.
    #Check every element in the range from index 1 to the final index.
    for num in range(1, len(gradeList)-1):
        #If the current number we are looking at is equal to the mode we have...
        if gradeList[num] == mode:
            #Add one to the mode count.
            modeCount += 1
        #If not...
        else:

            #We have to check and see if modeChallenge is -1
            if modeChallenge == -1:
                #This new element is a challenger, and will be saved as one
                modeChallenge = gradeList[num]
                #Increment the modeChallengeCount
                modeChallengeCount += 1

            #If it is the same as the current number, increment the challenge count
            elif modeChallenge == gradeList[num]:
                modeChallengeCount += 1

            #Finally, if neither is true, the new challenger is the current number.
            else:
                modeChallenge = gradeList[num]
                modeChallengeCount = -1

        #Now, let's check if our challenger's count is higher than the mode's count!
        if modeChallengeCount > modeCount:

            #The challenger becomes the new mode.
            mode = modeChallenge
            modeCount = modeChallengeCount

            #The challenger count and spot are reset
            modeChallenge = -1
            modeChallengeCount = 0

    print("The mode of this set of data is", str(mode)+".","It appeared", modeCount, "times!")

def main():

    #Let's first establish the grade so we can enter the loop
    grade = 1

    #Let's make a list to contain our grades.
    gradeList = []

    #While the grade is not negative, keep asking the user for values.
    while grade >= 0:

        #Make sure it is an integer. This can go on the same line or a different line.
        grade = int(input("Enter a grade (-1 to quit): "))

        #If the number is not negative, add it to the end of the list.
        if grade >= 0:
            gradeList.append(grade)

    #Finally, print the full list when you are finished entering the numbers.
    print("Grades:",gradeList)

    print()

    #Call the mean function and pass in the list that you have created.
    mean(gradeList)

    print()

    #Call the median function and pass in the list that you have created.
    median(gradeList)

    print()

    #Call the range function and pass in the list that you have created.
    Range(gradeList)

    print()

    #Finally, call the mode function and pass in the list that you have created.
    Mode(gradeList)

if __name__ == "__main__":
    main()
