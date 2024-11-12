import random
import sys


def secondNumber(digits):
    for i in range(len(digits)):
        if (i+1) % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                # print(f"Flagged {reverseddigits[i]}")
                modifieddigit = digits[i] // 10 + digits[i] % 10
                # print(modifieddigit)
                digits[i] = modifieddigit
    print(digits)
    print(f"Sum = {sum(digits)}")
    if sum(digits) % 10 == 0:
        print("The Input is Valid")
    else:
        print("Input is Invalid")


def luhnAlgorithm():
    while True:
        numbers = input("Enter your 11 Digit Account Number: ")
        digits = []

        if len(numbers) == 11:
            for digit in numbers:
                digits.append(int(digit))
            print(digits)
            secondNumber(digits)
        elif not numbers.isdigit():
            print("Exiting")
            sys.exit()
        else:
            print("Invalid input!\nDo you want to input another Value or Exit(X)?")


if __name__ == '__main__':
    luhnAlgorithm()