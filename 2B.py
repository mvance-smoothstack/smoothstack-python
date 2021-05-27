import math


def print_line():
    print("----------------------------------------")


first_list = []
first_list.append(1)
first_list.append("foo")
first_list.append(1.5)
print(first_list)
print_line()

second_list = [1, 1, [1, 2]]
print(second_list[2][1])
print_line()

third_list = ["a", "b", "c"]
print(third_list[1:])
print_line()

days_of_week = {"Sunday": 0, "Monday": 1, "Tuesday": 2,
                "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
print(days_of_week)
print_line()

D = {"k1": [1, 2, 3]}
print(D["k1"][1])
print_line()

first_tuple = 1, [2, 3]
print(first_tuple)
print_line()

# Was this question accidentally copied from 2A?
print("Mississippi".split())
print_line()

try:
    first_tuple[2] = "X"
except TypeError:
    print("Can't add to/modify tuples once they're created!")
print_line()

first_set = {1, 1, 2, 3}
print(first_set)  # should not show "1" twice
print_line()

# question 1
results = ""
for x in range(2000, 3201):
    if (x % 7 == 0) and not (x % 5 == 0):
        results += str(x) + ", "
print(results)
print_line()

# question 2
try:
    input_int = int(input("Enter an integer: "))
    print(str(input_int) + " factorial is: " + str(math.factorial(input_int)))
except ValueError:
    print("Integer not input! Skipping.")
print_line()

# question 3
try:
    input_dict_length = int(
        input("Enter how many squares you want to compute: "))
    if (input_dict_length < 1):
        print("Skipping.")
    else:
        square_dict = {}
        for x in range(1, input_dict_length + 1):
            square_dict[x] = x ** 2
        print(square_dict)
except ValueError:
    print("Integer not input! Skipping.")
print_line()

# question 4
try:
    input_numbers = input("Enter a list of integers separated by commas: ")
    if (input_numbers == ""):
        print("Skipping.")
    else:
        numbers_list = input_numbers.split(",")
        numbers_tuple = tuple(numbers_list)
        print(numbers_list)
        print(numbers_tuple)
except ValueError:
    print("Integer not input! Skipping.")
print_line()

# question 5


class InputOutString(object):
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())


instance = InputOutString()
instance.getString()
instance.printString()
