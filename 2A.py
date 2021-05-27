import math
import string


def print_line():
    print("----------------------------------------")


print("Hello World"[8])
print_line()
print("thinker"[2:5])
S = "hello"
print(S[1])
print_line()
S = "Sammy"
print(S[2:])
print_line()
print("Mississippi".split())
print_line()

lines = []
next = input("Input a potential palindrome, or blank line to end: ")
while next != '':
    lines.append(next)
    next = input("Input a potential palindrome, or blank line to end: ")

if len(lines) == 0:
    print("No lines entered! Aborting.")
else:
    answers = ""
    for line in lines:
        left = ""
        right = ""
        right_rev = ""
        formatted = ""
        # first, strip case
        line = line.lower()
        # strip whitespace and punctuation
        for character in line:
            if character in string.ascii_lowercase:
                formatted = formatted + character
        # determine the midpoint of the string
        midpoint = math.floor(len(formatted) / 2)
        # split the string
        if len(formatted) % 2 == 1:
            # if the string has an odd number of letters, compare everything before and everything after the middle character
            left = formatted[:midpoint]
            right = formatted[midpoint + 1:]
        else:
            # if the string has an even number of letters, there is no "middle character," so split it evenly
            left = formatted[:midpoint]
            right = formatted[midpoint:]
        # iterate over and reverse the right half of the string
        i = 0
        while i != len(right):
            i += 1
            right_rev = right_rev + right[-i]
        # now determine if it's a palindrome
        if left == right_rev:
            answers = answers + "Y "
        else:
            answers = answers + "N "
    print("Answer:")
    print(answers)
