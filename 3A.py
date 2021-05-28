import random


def print_line():
    print("----------------------------------------")


results = ""
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        results += str(x) + ", "
results = results[:-2]  # trim the last comma, because why not
print(results)
print_line()

scale = ''
while not (scale == 'f' or scale == 'c'):
    scale = input("Enter Fahrenheit or Celsius: ")
    scale = scale[0:1]
    scale = scale.lower()
temperature = None
while temperature == None:
    try:
        temperature = int(input("Enter a temperature: "))
    except ValueError:
        continue
        # do nothing, the program will prompt again
conv_temperature = None
if scale == 'f':
    conv_temperature = int((temperature - 32) / (9 / 5))
    print(str(temperature) + "°F is " + str(conv_temperature) + " in Celsius")
elif scale == 'c':
    conv_temperature = int((9 / 5) * temperature + 32)
    print(str(temperature) + "°C is " +
          str(conv_temperature) + " in Fahrenheit")
print_line()

the_number = random.randrange(1, 10)
win = False
while win == False:
    guess = None
    while guess == None:
        try:
            guess = int(input("Guess a number from 1 to 9: "))
        except ValueError:
            continue
    if guess == the_number:
        print("Well guessed!")
        win = True
print_line()

for x in range(1, 10):
    row = ""
    count = x
    if x > 5:
        count = 10 - x
    for y in range(1, count + 1):
        row = row + "* "
    print(row)
print_line()

the_word = None
while the_word == None:
    try:
        the_word = str(input("Enter a word: "))
    except ValueError:
        continue
reverse = ""
i = 0
while i != len(the_word):
    i += 1
    reverse = reverse + the_word[-i]
print(reverse)
print_line()

numbers = []
while True:
    try:
        next_num = input("Enter a number, or a blank line to finish: ")
        if next_num == "":
            break
        else:
            numbers.append(int(next_num))
    except ValueError:
        continue
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers: " + str(even))
print("Number of odd numbers: " + str(odd))
print_line()

datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print(item)
    print("Type: " + str(type(item)))
print_line()

output = ""
for x in range(0, 7):
    if x == 3 or x == 6:
        continue
    output = output + str(x) + " "
print(output)
