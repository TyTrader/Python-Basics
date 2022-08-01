# The range() function is used to loop around a set of code a specified number of times
# The range() function returns a sequence of numbers starting from 0 and increments by 1 by default

for x in range(10):
    print(x)  # prints all values from 0 to 9

# When using a start parameters

for x in range(5, 50):
    print(x)  # prints all values from 5 to 49

# Else in a for loop

for x in range(6):
    print(x)
else:  # When the loop is done, this block of code will be executed
    print("Yabba Dabba Doo")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")  # Will not be executed

    # Nested Loops

num = ['two', 'three', 'four']
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in num:
    for y in adj:
        for z in fruits:
            print(x, y, z)

    # The pass statement

for x in [0, 1, 2]:
    pass  # For loops cannot be empty
