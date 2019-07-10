def isPrime(num):
    if num < 4:
        return True
    else:
        for i in range(2, 6):
            if num%i == 0:
                return False
    return True

def main():
    num = int(input("Enter a number: "))
    result = isPrime(num)
    if result:
        print("This number is prime!")
    else:
        print("This number is not prime!")

main()