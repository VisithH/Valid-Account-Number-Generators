import random
import sys


def validator(digits):
    modifiedDigits = digits[:]
    for i in range(len(modifiedDigits)):
        if (i + 1) % 2 == 0:
            modifiedDigits[i] *= 2
            if modifiedDigits[i] > 9:
                # print(f"Flagged {reverseddigits[i]}")
                modifiedDigits[i] = modifiedDigits[i] // 10 + modifiedDigits[i] % 10
                # print(modifiedDigits)
    print(f"Modified = {modifiedDigits}")
    print(f"Sum = {sum(modifiedDigits)}")
    return sum(modifiedDigits)

# def luhnAlgorithm():
#     while True:
#         numbers = input("Enter your 11 Digit Account Number: ")
#         digits = []
#
#         if len(numbers) == 11:
#             for digit in numbers:
#                 digits.append(int(digit))
#             print(f"Original = {digits}")
#             validator(digits)
#             if sum(digits) % 10 == 0:
#                 print("The Input is Valid")
#             else:
#                 print("Input is Invalid")
#         elif not numbers.isdigit():
#             print("Exiting")
#             sys.exit()
#         else:
#             print("Invalid input!\nDo you want to input another Value or Exit(X)?")


def accountNumberGenerator():
    randomnumbers = []
    for i in range(10):
        numbers = random.randint(0, 9)
        randomnumbers.append(numbers)
    print(f"Original = {randomnumbers}")
    # print(sum(randomnumbers))
    checkedSum = validator(randomnumbers)

    # print(checkedrandomnumbers)
    if checkedSum % 10 == 0:
        randomnumbers.append(0)
        print("Account Number = ", *randomnumbers, sep='')
    else:
        total = checkedSum % 10
        # print(f"Modules = {total}")
        remainder = 10 - total
        print(f"remainder = {remainder}")
        randomnumbers.append(remainder)
        print("Account Number = ", *randomnumbers, sep='')


# luhnAlgorithm()
accountNumberGenerator()
