def main():
    x = int(input("Enter num 1: "))
    y = int(input("Enter num 2: "))
    z = int(input("Enter num 3: "))

    largest = 0

    if x > y and x > z:
        largest = x
    elif y > x and y > z:
        largest = y
    elif z > x and z > y:
        largest = z

    print(str(largest)+" is the largest number!")

main()