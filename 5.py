# While loops are used to execute a set of statements as long as a condition is true

i = 1
while i < 10:
    print(i)
    i += 1  # It will output numbers between 1 and 5 in a column

i = 1
while i < 100:
    print(i)
    i += 1  # It will output numbers between 1 and 99

i = 1
while i < 100:
    print(i)
    i -= 1
    break

# Else statements within while loops

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# FOR LOOPS are used to iterate over a sequence. No need for an index variable

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

    # looping through a string

for x in "banana":
    print(x)

    # The break statements

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":  # Exit the loop when x is 'banana'
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":  # Exit the loop when x is 'banana' but before the print so only apple will be printed
        break
    print(x)

    # The continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":  # Banana will not be printed
        continue
    print(x)
