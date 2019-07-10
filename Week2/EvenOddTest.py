def isEvenOdd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

def main():
    num = input("Enter a number: ")
    num = int(num)
    result = isEvenOdd(num)
    print("This number is "+result)

main()