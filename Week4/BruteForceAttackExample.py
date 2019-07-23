'''
In this kind of breach, you continuously guess the password until one is the correct one.
'''


#Here is the full alphabet, in uppercase and lowercase
UPPER_ALPHABET = "AABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

#Here is the empty string that the password will be stored in.
passowrd = ""


'''
We know three things about the password...
1. It starts with a capital letter
2. There is a lowercase letter immediately afterward
3. There are six digits

We can use nested for loops to find the correct password. It will take some time, but it still works after a while.
'''


#
for i in UPPER_ALPHABET:
    for j in LOWER_ALPHABET:
        for k in range(1000000):
            password = i+j
            numChar = str(k)
            numLen = len(numChar)
            password = password + ("0" * (6-numLen)) + numChar
            print(password)
            if password == "Gy157027":
                print("Password found")

