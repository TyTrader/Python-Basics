# The Python Function

def my_function():
    print('War never changes anything')


my_function()


# Arguments within the function

def my_function(Fname):
    print(Fname + ' is being called upon')


my_function('Zhukov')
my_function('Konev')
my_function('Rokossovsky')

"""
Arguments are shortened to args within python.
From a function's perspective: 
A parameter is the variable listed inside the parentheses in the function 
definition. 
An argument is the value that is sent to the function when it is called. 
"""

# Number of args
"""By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, you have to call the function 
with 2 arguments, not more, and not less."""


def my_function(fname, lname):
    print(fname + " " + lname)


my_function('Mo', 'Salah')

# Arbitray arguments
"""If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition. 
This way the function will receive a tuple of arguments, and can access the 
items accordingly: """


def my_function(*cars):
    print('The fastest car is ' + cars[2])


my_function('Bugatti', 'Pagani', 'Koenigsegg')

# Keyword Arguments
"""You can also send arguments with the key = value syntax. 
This way the order of the arguments does not matter."""


def my_function(bus1, bus2, bus3):
    print(
        'The best bus company is ' + bus3 + ' and the worst bus company is ' + bus1 + ' and the busiest bus company is ' + bus2)


my_function(bus1='Starbus', bus2='Hoppa', bus3='Rembo')

# Arbitray arguments
"""If you do not know how many keyword arguments that will be passed into your 
function, add two asterisk: ** before the parameter name in the function 
definition. 
This way the function will receive a dictionary of arguments, and can access the 
items accordingly:"""


def my_function(**actor):
    print('The best actor award goes to ' + actor['fname'] + actor['lname'])


my_function(fname='Samuel', lname=' Jackson')

# Default parameter
"""The following example shows how to use a default parameter value. 
If we call the function without argument, it uses the default value: """


def my_function(car="Ferrari"):
    print('The fastest sports car is a  ' + car)


my_function('maserati')
my_function('aston martin')
my_function('alfa romeo')
my_function()

# Passing a list as an argument
"""You can send any data types of argument to a function (string, number, list, 
dictionary etc.), and it will be treated as the same data type inside the function. 
E.g. if you send a List as an argument, it will still be a List when it reaches the 
function:"""


def my_function(mountains):
    for x in mountains:
        print(x)


mountains = ['kirinyaga', 'kilimanjaro', 'elgon', 'ruwenzori']
my_function(mountains)
