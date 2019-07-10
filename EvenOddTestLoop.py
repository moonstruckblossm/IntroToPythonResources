def isEvenOdd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

def main():
    while True:
        num = input("Enter a number: ")
        if num == "quit":
            print("Goodbye!")
            break
        else:
            num = int(num)
            result = isEvenOdd(num)
            print("This number is "+result)

main()