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

    #Finally, print the mean.
    print("The mean of this set of data is ", mean)


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
    print(gradeList)

    #Call the mean function and pass in the list that you have created.
    mean(gradeList)


if __name__ == "__main__":
    main()
